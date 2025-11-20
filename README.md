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


<table>
  <tr>
    <th>Dataset</th>
    <th>HOTA</th>
    <th>IDF1</th>
    <th>Assa</th>
    <th>MOTA</th>
    <th>DetA</th>
  </tr>

  <!-- DanceTrack 블록 (바깥 테이블) -->
  <tr>
    <!-- 1열의 2행 전체를 담당하는 셀 -->
    <td rowspan="3" style="padding:0;">
      <!-- 안쪽에 작은 테이블로 2열 + (2열의 2행) 구성 -->
      <table style="border-collapse:collapse; width:100%; height:100%;">
        <tr>
          <!-- 왼쪽 열 (DanceTrack) : 세로로 두 줄을 차지 -->
          <td rowspan="2" style="border:1px solid #444; padding:4px;">DanceTrack</td>
          <!-- 오른쪽 열의 첫 번째 행 -->
          <td style="border:1px solid #444; padding:4px;">서브 1</td>
        </tr>
        <tr>
          <!-- 오른쪽 열의 두 번째 행 -->
          <td style="border:1px solid #444; padding:4px;">서브 2</td>
        </tr>
      </table>
    </td>

    <!-- 나머지 열들 -->
    <td>62.3</td>
    <td>63.0</td>
    <td>47.2</td>
    <td>92.8</td>
    <td>82.5</td>
  </tr>

  <!-- DanceTrack 두 번째 줄 -->
  <tr>
    <td colspan="5">여기에 두 번째 줄 내용</td>
  </tr>

  <!-- DanceTrack 세 번째 줄 -->
  <tr>
    <td colspan="5">여기에 세 번째 줄 내용</td>
  </tr>

  <tr>
    <td>SportsMOT</td>
    <td>76.2</td>
    <td>76.1</td>
    <td>65.1</td>
    <td>97.1</td>
    <td>89.3</td>
  </tr>
  <tr>
    <td>MOT17</td>
    <td>64.5</td>
    <td>79.3</td>
    <td>64.6</td>
    <td>79.8</td>
    <td>64.7</td>
  </tr>
  <tr>
    <td>MOT20</td>
    <td>61.7</td>
    <td>74.9</td>
    <td>60.5</td>
    <td>76.7</td>
    <td>63.2</td>
  </tr>
</table>


## 🚀 Tracking performance

PlugTrack(DiffMOT)
| Dataset    |  HOTA | IDF1 | Assa | MOTA | DetA | 
|--------------|-----------|--------|-------|----------|----------|
|DanceTrack  | 62.3 | 63.0 | 47.2 | 92.8 | 82.5 | 
|SportsMOT   | 76.2 | 76.1 | 65.1 | 97.1 | 89.3 | 
|MOT17       | 64.5 | 79.3 | 64.6 | 79.8 | 64.7 | 
|MOT20       | 61.7 | 74.9 | 60.5 | 76.7 | 63.2 | 

PlugTrack(TrackSSM)
| Dataset    |  HOTA | IDF1 | Assa | MOTA | DetA | 
|--------------|-----------|--------|-------|----------|----------|
|DanceTrack  | 62.3 | 63.0 | 47.2 | 92.8 | 82.5 | 
|SportsMOT   | 76.2 | 76.1 | 65.1 | 97.1 | 89.3 | 
|MOT17       | 64.5 | 79.3 | 64.6 | 79.8 | 64.7 | 
|MOT20       | 61.7 | 74.9 | 60.5 | 76.7 | 63.2 |