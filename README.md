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
  <h3 align="center"><a href="https://arxiv.org/abs/2511.13105">Paper</a> | <a href="https://github.com/VisualScienceLab-KHU/PlugTrack?tab=readme-ov-file">Project Page</a> | <a href="https://drive.google.com/drive/folders/10wlyUog-jtK87P4TFUKNEKOLuxjPBdJi?usp=drive_link">Pretrained Models</a> </h3>

<br>
</p>

<p align="center">
  <img src="./img/figure1.png" width="800">
</p>


## 🚀 Tracking performance

PlugTrack(DiffMOT)

<table>
  <tr>
    <th colspan="2">Dataset</th>
    <th>HOTA</th>
    <th>IDF1</th>
    <th>AssA</th>
    <th>MOTA</th>
    <th>DetA</th>
  </tr>

  <!-- DanceTrack -->
  <tr>
    <td rowspan="2">DanceTrack</td>
    <td>Base</td>
    <td>62.3</td>
    <td>63.0</td>
    <td>47.2</td>
    <td>92.8</td>
    <td>82.5</td>
  </tr>
  <tr>
    <td>Ours</td>
    <td>63.3</td>
    <td>64.1</td>
    <td>48.4</td>
    <td>92.4</td>
    <td>82.5</td>
  </tr>

  <!-- MOT17 -->
  <tr>
    <td rowspan="2">MOT17</td>
    <td>Base</td>
    <td>64.0</td>
    <td>78.9</td>
    <td>64.2</td>
    <td>79.1</td>
    <td>64.1</td>
  </tr>
  <tr>
    <td>Ours</td>
    <td>64.2</td>
    <td>79.0</td>
    <td>64.4</td>
    <td>79.2</td>
    <td>74.0</td>
  </tr>

  <!-- MOT20 -->
  <tr>
    <td rowspan="2">MOT20</td>
    <td>Base</td>
    <td>61.6</td>
    <td>74.9</td>
    <td>60.5</td>
    <td>76.3</td>
    <td>62.8</td>
  </tr>
  <tr>
    <td>Ours</td>
    <td>61.8</td>
    <td>75.2</td>
    <td>60.9</td>
    <td>76.4</td>
    <td>62.9</td>
  </tr>
</table>

PlugTrack(TrackSSM)

<table>
  <tr>
    <th colspan="2">Dataset</th>
    <th>HOTA</th>
    <th>IDF1</th>
    <th>AssA</th>
    <th>MOTA</th>
    <th>DetA</th>
  </tr>

  <!-- DanceTrack -->
  <tr>
    <td rowspan="2">DanceTrack</td>
    <td>Base</td>
    <td>57.7</td>
    <td>57.5</td>
    <td>41.0</td>
    <td>92.2</td>
    <td>81.5</td>
  </tr>
  <tr>
    <td>Ours</td>
    <td>59.2</td>
    <td>59.0</td>
    <td>42.9</td>
    <td>92.2</td>
    <td>81.9</td>
  </tr>

  <!-- MOT17 -->
  <tr>
    <td rowspan="2">MOT17</td>
    <td>Base</td>
    <td>61.4</td>
    <td>74.1</td>
    <td>59.6</td>
    <td>78.5</td>
    <td>63.6</td>
  </tr>
  <tr>
    <td>Ours</td>
    <td>61.9</td>
    <td>75.2</td>
    <td>60.3</td>
    <td>78.7</td>
    <td>63.9</td>
  </tr>

  <!-- MOT20 -->
  <tr>
    <td rowspan="2">MOT20</td>
    <td>Base</td>
    <td>59.1</td>
    <td>71.1</td>
    <td>57.5</td>
    <td>73.9</td>
    <td>60.9</td>
  </tr>
  <tr>
    <td>Ours</td>
    <td>59.7</td>
    <td>72.3</td>
    <td>58.5</td>
    <td>61.3</td>
    <td>74.5</td>
  </tr>
</table>

## 🧩 Usage

PlugTrack is designed as a **plug-and-play module** that can be seamlessly integrated into existing multi-object tracking pipelines.  
All core components, feature extractors, and fusion modules are provided in the **`assets/`** directory.

- **Full implementation:**  
  👉 [`assets/`](https://github.com/VisualScienceLab-KHU/PlugTrack/tree/main/assets)

PlugTrack supports both **TrackSSM** and **DiffMOT**.  
We provide minimal working examples demonstrating how to plug PlugTrack into each framework:

- **PlugTrack + TrackSSM example:**  
  👉 [`example_autoencoder_trackssm.py`](https://github.com/VisualScienceLab-KHU/PlugTrack/blob/main/example_autoencoder_trackssm.py)

- **PlugTrack + DiffMOT example:**  
  👉 [`example_autoencoder_diffmot.py`](https://github.com/VisualScienceLab-KHU/PlugTrack/blob/main/example_autoencoder_diffmot.py)

Each example illustrates:
- how to import and initialize the PlugTrack fusion module  
- how to attach it to the base model (TrackSSM or DiffMOT)  
- how to run the end-to-end tracking pipeline with PlugTrack integrated

You can extend these templates to integrate PlugTrack with other detectors or trackers.  
**Contributions and plug-in adapters for new models are welcome!**
