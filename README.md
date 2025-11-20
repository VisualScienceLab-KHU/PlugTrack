<p align="center">
  <h1 align="center">PlugTrack: Multi-Perceptive Motion Analysis <br> for Adaptive Fusion in Multi-Object Tracking
</h1>
  <p align="center">
    <a href="https://tmdwo8814.github.io/">Seungjae Kim</a>
    &nbsp;·&nbsp;
    <a href="https://my.surfit.io/w/1720083748">SeungJoon Lee</a>
    &nbsp;·&nbsp;
    <a href="https://myeongahcho.netlify.app/">MyeongAh Cho</a>
    &nbsp;·&nbsp;
  </p>
  <h3 align="center">AAAI 2026</h3>
  <h3 align="center"><a href="https://arxiv.org/abs/2511.13105">Paper</a> | <a href="https://github.com/VisualScienceLab-KHU/PlugTrack?tab=readme-ov-file">Project Page</a> | <a href="https://github.com/VisualScienceLab-KHU/PlugTrack?tab=readme-ov-file">Pretrained Models</a> </h3>

<br>
</p>

<p align="center">
  <img src="./img/figure1.png" width="800">
</p>

## 🚀 Tracking performance
### Benchmark Evaluation 
PlugTrack(DiffMOT)
| Dataset    |  HOTA | IDF1 | Assa | MOTA | DetA | Weight | Results |
|--------------|-----------|--------|-------|----------|----------|----------|----------|
|DanceTrack  | 62.3 | 63.0 | 47.2 | 92.8 | 82.5 | [download](https://github.com/Kroery/DiffMOT/releases/download/v1.0/DanceTrack_epoch800.pt) | [DanceTrack_Results](https://github.com/Kroery/DiffMOT/releases/download/v1.2/DanceTrack_DiffMOT.zip)|
|SportsMOT   | 76.2 | 76.1 | 65.1 | 97.1 | 89.3 | [download](https://github.com/Kroery/DiffMOT/releases/download/v1.0/SportsMOT_epoch1200.pt) | [SportsMOT_Results](https://github.com/Kroery/DiffMOT/releases/download/v1.2/SportsMOT_DiffMOT.zip)|
|MOT17       | 64.5 | 79.3 | 64.6 | 79.8 | 64.7 | [download](https://github.com/Kroery/DiffMOT/releases/download/v1.0/MOT_epoch800.pt) | [MOT17_Results](https://github.com/Kroery/DiffMOT/releases/download/v1.2/MOT17_DiffMOT.zip)|
|MOT20       | 61.7 | 74.9 | 60.5 | 76.7 | 63.2 | [download](https://github.com/Kroery/DiffMOT/releases/download/v1.0/MOT_epoch800.pt) | [MOT20_Results](https://github.com/Kroery/DiffMOT/releases/download/v1.2/MOT20_DiffMOT.zip)|

PlugTrack(TrackSSM)
| Dataset    |  HOTA | IDF1 | Assa | MOTA | DetA | Weight | Results |
|--------------|-----------|--------|-------|----------|----------|----------|----------|
|DanceTrack  | 62.3 | 63.0 | 47.2 | 92.8 | 82.5 | [download](https://github.com/Kroery/DiffMOT/releases/download/v1.0/DanceTrack_epoch800.pt) | [DanceTrack_Results](https://github.com/Kroery/DiffMOT/releases/download/v1.2/DanceTrack_DiffMOT.zip)|
|SportsMOT   | 76.2 | 76.1 | 65.1 | 97.1 | 89.3 | [download](https://github.com/Kroery/DiffMOT/releases/download/v1.0/SportsMOT_epoch1200.pt) | [SportsMOT_Results](https://github.com/Kroery/DiffMOT/releases/download/v1.2/SportsMOT_DiffMOT.zip)|
|MOT17       | 64.5 | 79.3 | 64.6 | 79.8 | 64.7 | [download](https://github.com/Kroery/DiffMOT/releases/download/v1.0/MOT_epoch800.pt) | [MOT17_Results](https://github.com/Kroery/DiffMOT/releases/download/v1.2/MOT17_DiffMOT.zip)|
|MOT20       | 61.7 | 74.9 | 60.5 | 76.7 | 63.2 | [download](https://github.com/Kroery/DiffMOT/releases/download/v1.0/MOT_epoch800.pt) | [MOT20_Results](https://github.com/Kroery/DiffMOT/releases/download/v1.2/MOT20_DiffMOT.zip)|