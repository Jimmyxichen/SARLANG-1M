<div align="center">
<h1 align="center">☀️SARLANG-1M☀️</h1>

<h3>SARLANG-1M: A Benchmark for Vision-Language Modeling in SAR Image Understanding</h3>

[Yimin Wei](https://www.researchgate.net/profile/Yimin-Wei-9)<sup>1,2</sup>, [Aoran Xiao](https://scholar.google.com/citations?hl=ja&user=yGKsEpAAAAAJ)<sup>2</sup>, [Yexian Ren](https://scholar.google.com/citations?user=xX1c-SwAAAAJ&hl=en)<sup>3</sup>, [Yuting Zhu](https://scholar.google.com/citations?user=2G9RsM0AAAAJ&hl=zh-CN)<sup>4</sup>,  
[Hongruixuan Chen](https://scholar.google.ch/citations?user=XOk4Cf0AAAAJ&hl=zh-CN&oi=ao)<sup>1,2</sup>, [Junshi Xia](https://scholar.google.com/citations?user=n1aKdTkAAAAJ&hl=en)<sup>2</sup>, [Naoto Yokoya](https://scholar.google.co.jp/citations?user=DJ2KOn8AAAAJ&hl=en)<sup>1,2 *</sup>

<sup>1</sup> The University of Tokyo, <sup>2</sup> RIKEN AIP,  <sup>3</sup> Nanjing University of Information Science and Technology,  <sup>4</sup> Sun Yat-sen University

[![arXiv paper](https://img.shields.io/badge/arXiv-paper-b31b1b.svg)](https://arxiv.org/abs/2504.03254)   [![HuggingFace Dataset](https://img.shields.io/badge/HuggingFace-Dataset-yellow)](https://huggingface.co/datasets/YiminJimmy/SARLANG-1M)

</div>

## 🔭Overview

* [**SARLANG-1M**](https://arxiv.org/abs/2504.03254) is a large-scale benchmark tailored for multimodal SAR image understanding, with a primary focus on integrating SAR with textual modality. SARLANG-1M comprises more than 1 million high-quality SAR image-text pairs collected from over 59 cities worldwide. It features hierarchical resolutions (ranging from 0.1 to 25 meters), fine-grained semantic descriptions (including both concise and detailed captions), diverse remote sensing categories (1,696 object types and 16 land cover classes), and multi-task question-answering pairs spanning seven applications and 1,012 question types. Extensive experiments on mainstream VLMs demonstrate that fine-tuning with SARLANG-1M significantly enhances their performance in SAR image interpretation, reaching performance comparable to human experts.

<p align="center">
  <img src="Overview.png" alt="accuracy" width="97%">
</p>

## 🗝️Let's Get Started with SARLANG-1M!
### `A. Installation`

Note that the code in this repo runs under **Linux** system. We have not tested whether it works under other OS.

**Step 1: Clone the repository:**

Clone this repository and navigate to the project directory:
```bash
git clone https://github.com/Jimmyxichen/SARLANG-1M.git
cd SARLANG-1M
```

**Step 2: Environment Setup:**

It is recommended to set up a conda environment and installing dependencies via pip. Use the following commands to set up your environment:

***Create and activate a new conda environment***

```bash
conda create -n SARLANG1M
conda activate SARLANG1M
```

***Install dependencies***

```bash
pip install -r requirements.txt
```

### `B. Data Preparation`

### `C. Model Training & Tuning`

### `D. Inference & Evaluation`

## 📜Reference

If this dataset or code contributes to your research, please kindly consider citing our paper and give this repo ⭐️.

## 🤝Acknowledgments
The authors would also like to give special thanks to [SARDet_100K](https://github.com/zcablii/SARDet_100K), [SpaceNet6](https://spacenet.ai/sn6-challenge/), [DFC2023](https://www.grss-ieee.org/community/technical-committees/2023-ieee-grss-data-fusion-contest/) and [OpenEarthMap-SAR](https://zenodo.org/records/14622048) for providing the valuable SAR Images.

## 🙋Q & A
***For any questions, please feel free to leave it in the [issue section](https://github.com/Jimmyxichen/SARLANG-1M/issues) or [contact us.](2364356729@qq.com)***
