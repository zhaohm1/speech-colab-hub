# 开源语音模型 Google Colab Notebook Hub

用 Google Colab 快速体验开源 ASR/TTS 模型的单样本推理。Notebook 保留模型来源、依赖与环境记录；单次体验不代表准确率或稳定性能评测。仓库已公开，Notebook 可直接从 Colab 打开。

## ASR

| 模型 | 功能 | 运行环境 | 来源 | 验证状态 | Notebook | Colab |
| --- | --- | --- | --- | --- | --- | --- |
| Whisper small | 上传音频并转写 | Colab GPU，推荐 T4 | [官方代码](https://github.com/openai/whisper)、[模型说明](https://github.com/openai/whisper#available-models-and-languages)；MIT | `verified`：T4 单样本推理，见[验证记录](validation/whisper_colab_t4_20261114.md) | [查看 Notebook](notebooks/asr/whisper.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zhaohm1/speech-colab-hub/blob/main/notebooks/asr/whisper.ipynb) |

## TTS

| 模型 | 功能 | 运行环境 | 来源 | 验证状态 | Notebook | Colab |
| --- | --- | --- | --- | --- | --- | --- |
| CosyVoice3 0.5B | 输入文本、合成并试听 WAV；复用 Colab PyTorch/CUDA | Colab GPU；模型约 9.8 GB，建议至少 18 GiB 空闲磁盘 | [官方代码](https://github.com/FunAudioLLM/CosyVoice)、[模型页](https://www.modelscope.cn/models/FunAudioLLM/Fun-CosyVoice3-0.5B-2512)；Apache-2.0（模型卡标注） | `unverified`：[首次运行停在哈希校验](validation/cosyvoice3_colab_failure_20261114.md)，尚无合成结果 | [查看 Notebook](notebooks/tts/cosyvoice3.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zhaohm1/speech-colab-hub/blob/main/notebooks/tts/cosyvoice3.ipynb) |

## 在 Colab 打开

点击表格中的 **Open in Colab**，选择 GPU 运行时后按顺序执行。若 Colab 的 GitHub 入口暂时无法加载，也可从 GitHub 下载对应 Notebook，在 Colab 选择 **File → Upload notebook** 打开副本。

## 使用与证据

打开 Notebook，选择 GPU 运行时，按顺序执行各单元并上传音频或输入文本。依赖会在 Colab 中安装，模型下载到显式指定的临时目录。不要在 Notebook 中填写访问令牌。运行成功后记录输出、单次耗时、显存与版本；未经 GPU 实测的条目保持 `unverified`。模板与生成、静态检查方式见 [设计说明](DESIGN.md)。
