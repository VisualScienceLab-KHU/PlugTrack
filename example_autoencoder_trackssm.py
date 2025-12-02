import torch
from torch.nn import Module
import torch.nn as nn
from models.motion_decoder import Time_info_decoder
import numpy as np
import torch.nn.functional as F

from assets.contextual_motion_encoder import ContextualMotionEncoder
from assets.blender import AdaptiveBlendingWeightGenerator
from assets.kalman_filter import KalmanFilter

class D2MP(Module):
    def __init__(self, config, encoder=None, device="cuda"):
        super().__init__()
        self.config = config
        self.device = device
        self.encoder = encoder
        self.ssm_decoder = Time_info_decoder()

        self.contextual_motion_encoder = ContextualMotionEncoder()
        self.adaptive_blending_generator = AdaptiveBlendingWeightGenerator()
        self.kf = KalmanFilter(device, 1e-5, 5e-4)

    def generate(self, conds, sample, bestof, flexibility=0.0, ret_traj=False, img_w=None, img_h=None):
        cond_encodeds = []
        for i in range(len(conds)):
            tmp_c = conds[i]
            tmp_c = np.array(tmp_c)
            tmp_c[:, 0::2] = tmp_c[:, 0::2] / img_w
            tmp_c[:, 1::2] = tmp_c[:, 1::2] / img_h
            tmp_conds = torch.tensor(tmp_c, dtype=torch.float)
            if len(tmp_conds) != self.config.interval:
                pad_conds = tmp_conds[-1].repeat((self.config.interval, 1))
                tmp_conds = torch.cat((tmp_conds, pad_conds), dim=0)[:self.config.interval]
            cond_encodeds.append(tmp_conds.unsqueeze(0))
        cond_encodeds = torch.cat(cond_encodeds).to(self.device)

        B = cond_encodeds.shape[0]
        history = cond_encodeds.reshape(B, -1)

        # trackssm
        mamba_f = self.encoder(cond_encodeds)
        bbox_mp = self.ssm_decoder(cond_encodeds[:, -1, :4], mamba_f)

        # KF
        bbox_kf, kf_uncertainty = self.kf.predict(cond_encodeds)

        f_context = self.contextual_motion_encoder(cond_encodeds, bbox_kf, bbox_mp, kf_uncertainty)
        bbox_final, _, _, _, _ = self.adaptive_blending_generator(f_context, bbox_kf, bbox_mp, None, False)

        return bbox_mp.cpu().detach().numpy()

    def forward(self, batch, epoch):
        cond = batch['condition']
        bbox_gt = batch['cur_bbox']

        B = cond.size(0)
        history = cond.reshape(B, -1)

        # trackssm
        mamba_f  = self.encoder(cond)
        bbox_mp, loss_mp  = self.ssm_decoder(cond[:, -1, :4], 
                                   mamba_f,
                                   curr_gt=bbox_gt)
        # kf
        bbox_kf, kf_uncertainty = self.kf.predict(cond)

        f_context = self.contextual_motion_encoder(cond, bbox_kf, bbox_mp, kf_uncertainty)
        bbox_final, predicted_alpha, optimal_alpha, loss_final, predictor_loss = self.adaptive_blending_generator(f_context, bbox_kf, bbox_mp, bbox_gt, True)

        loss_total = loss_final + predictor_loss
        return loss_total

def compute_iou(pred, targets):
    pred_x1 = pred[..., 0]
    pred_y1 = pred[..., 1]
    pred_x2 = pred[..., 0] + pred[..., 2]
    pred_y2 = pred[..., 1] + pred[..., 3]
    
    target_x1 = targets[..., 0]
    target_y1 = targets[..., 1]
    target_x2 = targets[..., 0] + targets[..., 2]
    target_y2 = targets[..., 1] + targets[..., 3]
    
    inter_x1 = torch.max(pred_x1, target_x1)
    inter_y1 = torch.max(pred_y1, target_y1)
    inter_x2 = torch.min(pred_x2, target_x2)
    inter_y2 = torch.min(pred_y2, target_y2)
    
    inter_w = (inter_x2 - inter_x1).clamp(min=0)
    inter_h = (inter_y2 - inter_y1).clamp(min=0)
    inter_area = inter_w * inter_h
    
    pred_area = pred[..., 2] * pred[..., 3]
    target_area = targets[..., 2] * targets[..., 3]
    
    union_area = pred_area + target_area - inter_area + 1e-10  
    iou = inter_area / union_area
    return iou

def compute_giou(pred, targets):
    pred_x1 = pred[..., 0]
    pred_y1 = pred[..., 1]
    pred_x2 = pred[..., 0] + pred[..., 2]
    pred_y2 = pred[..., 1] + pred[..., 3]

    target_x1 = targets[..., 0]
    target_y1 = targets[..., 1]
    target_x2 = targets[..., 0] + targets[..., 2]
    target_y2 = targets[..., 1] + targets[..., 3]

    inter_x1 = torch.max(pred_x1, target_x1)
    inter_y1 = torch.max(pred_y1, target_y1)
    inter_x2 = torch.min(pred_x2, target_x2)
    inter_y2 = torch.min(pred_y2, target_y2)

    inter_area = (inter_x2 - inter_x1).clamp(min=0) * (inter_y2 - inter_y1).clamp(min=0)

    pred_area = (pred_x2 - pred_x1) * (pred_y2 - pred_y1)
    target_area = (target_x2 - target_x1) * (target_y2 - target_y1)

    union_area = pred_area + target_area - inter_area + 1e-10
    iou = inter_area / union_area

    enc_x1 = torch.min(pred_x1, target_x1)
    enc_y1 = torch.min(pred_y1, target_y1)
    enc_x2 = torch.max(pred_x2, target_x2)
    enc_y2 = torch.max(pred_y2, target_y2)

    enc_area = (enc_x2 - enc_x1) * (enc_y2 - enc_y1) + 1e-10

    giou = iou - (enc_area - union_area) / enc_area

    return giou