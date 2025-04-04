<div align="center">
<h1 align="center">☀️SARLANG-1M☀️</h1>

<h3>SARLANG-1M: A Benchmark for Vision-Language Modeling in SAR Image Understanding</h3>

[Yimin Wei](https://www.researchgate.net/profile/Yimin-Wei-9)<sup>1,2</sup>, [Aoran Xiao](https://scholar.google.com/citations?hl=ja&user=yGKsEpAAAAAJ)<sup>2</sup>, [Yexian Ren](https://scholar.google.com/citations?user=xX1c-SwAAAAJ&hl=en)<sup>3</sup>, [Yuting Zhu](https://scholar.google.com/citations?user=2G9RsM0AAAAJ&hl=zh-CN)<sup>4</sup>,  
[Hongruixuan Chen](https://scholar.google.ch/citations?user=XOk4Cf0AAAAJ&hl=zh-CN&oi=ao)<sup>1,2</sup>, [Junshi Xia](https://scholar.google.com/citations?user=n1aKdTkAAAAJ&hl=en)<sup>2</sup>, [Naoto Yokoya](https://scholar.google.co.jp/citations?user=DJ2KOn8AAAAJ&hl=en)<sup>1,2 *</sup>

<sup>1</sup> The University of Tokyo, <sup>2</sup> RIKEN AIP,  <sup>3</sup> Nanjing University of Information Science and Technology,  <sup>4</sup> Sun Yat-sen University

[![HuggingFace Dataset](https://img.shields.io/badge/HuggingFace-Dataset-yellow)](https://huggingface.co/datasets/YiminJimmy/SARLANG-1M)

</div>

# SARLANG-1M
SARLANG-1M is a large-scale benchmark tailored for multimodal SAR image understanding, with a primary focus on integrating SAR with textual modality. SARLANG-1M comprises more than 1 million high-quality SAR image-text pairs collected from over 59 cities worldwide. It features hierarchical resolutions (ranging from 0.1 to 25 meters), fine-grained semantic descriptions (including both concise and detailed captions), diverse remote sensing categories (1,696 object types and 16 land cover classes), and multi-task question-answering pairs spanning seven applications and 1,012 question types. Extensive experiments on mainstream VLMs demonstrate that fine-tuning with SARLANG-1M significantly enhances their performance in SAR image interpretation, reaching performance comparable to human experts.

<p align="center">
  <img src="Overview.png" alt="accuracy" width="97%">
</p>
