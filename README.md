# 开源语音模型 Google Colab Notebook Hub

用 Google Colab 快速体验开源 ASR/TTS 模型的单样本推理。Notebook 保留模型来源、依赖与环境记录；单次体验不代表准确率或稳定性能评测。仓库已公开，Notebook 可直接从 Colab 打开。

## ASR

| 模型 | 功能 | 运行环境 | 来源 | 验证状态 | Notebook | Colab |
| --- | --- | --- | --- | --- | --- | --- |
| Whisper small | 上传音频并转写 | Colab GPU，推荐 T4 | [官方代码](https://github.com/openai/whisper)、[模型说明](https://github.com/openai/whisper#available-models-and-languages)；MIT | `verified`：T4 单样本推理，见[验证记录](validation/whisper_colab_t4_20261114.md) | [查看 Notebook](notebooks/asr/whisper.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zhaohm1/speech-colab-hub/blob/main/notebooks/asr/whisper.ipynb) |
| Confucius4-R2T2 | 上传音频，按 160 ms 分块查看稳定前缀和最终转写 | Colab GPU，vLLM；建议至少 12 GiB 空闲磁盘 | [官方代码](https://github.com/netease-youdao/Confucius4-R2T2)、[模型权重](https://huggingface.co/netease-youdao/Confucius4-R2T2)；代码 Apache-2.0，[权重另有许可](https://github.com/netease-youdao/Confucius4-R2T2/blob/master/MODEL_LICENSE) | `unverified`：尚无 Colab GPU 实测 | [查看 Notebook](notebooks/asr/confucius4_r2t2.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zhaohm1/speech-colab-hub/blob/main/notebooks/asr/confucius4_r2t2.ipynb) |

## TTS

| 模型 | 功能 | 运行环境 | 来源 | 验证状态 | Notebook | Colab |
| --- | --- | --- | --- | --- | --- | --- |
| CosyVoice3 0.5B | 输入文本、直接合成并试听 WAV；复用 Colab PyTorch/CUDA | Colab T4；半精度加载，模型约 9.8 GB，建议至少 18 GiB 空闲磁盘 | [官方代码](https://github.com/FunAudioLLM/CosyVoice)、[模型页](https://www.modelscope.cn/models/FunAudioLLM/Fun-CosyVoice3-0.5B-2512)；Apache-2.0（模型卡标注） | `verified`：[T4 单句合成记录](validation/cosyvoice3_colab_t4_20261115.md)；[首次哈希失败记录](validation/cosyvoice3_colab_failure_20261114.md) | [查看 Notebook](notebooks/tts/cosyvoice3.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zhaohm1/speech-colab-hub/blob/main/notebooks/tts/cosyvoice3.ipynb) |
| Qwen3-TTS VoiceDesign 1.7B | 自然语言描述音色、合成并试听 | Colab GPU；建议至少 12 GiB 空闲磁盘 | [官方代码](https://github.com/QwenLM/Qwen3-TTS)、[模型页](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign)；Apache-2.0 | `unverified`：尚无 Colab GPU 实测 | [查看 Notebook](notebooks/tts/qwen3_tts_voice_design.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zhaohm1/speech-colab-hub/blob/main/notebooks/tts/qwen3_tts_voice_design.ipynb) |
| VoxCPM2 | 括号内描述音色、合成并试听 | Colab GPU；建议至少 12 GiB 空闲磁盘 | [官方代码](https://github.com/OpenBMB/VoxCPM)、[模型页](https://huggingface.co/openbmb/VoxCPM2)；Apache-2.0 | `unverified`：尚无 Colab GPU 实测 | [查看 Notebook](notebooks/tts/voxcpm2.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zhaohm1/speech-colab-hub/blob/main/notebooks/tts/voxcpm2.ipynb) |
| IndexTTS-2.5 | 参考音频音色克隆、8 维情绪向量控制 | Colab 连接 Python 3.10–3.11 GPU 本地运行时；默认托管运行时不兼容 | [官方代码](https://github.com/index-tts/index-tts)、[模型页](https://huggingface.co/IndexTeam/IndexTTS-2.5)；[bilibili Model Use License Agreement](https://github.com/index-tts/index-tts/blob/main/LICENSE) | `unverified`：需兼容 Python 运行时及 GPU 实测 | [查看 Notebook](notebooks/tts/indextts2_5.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zhaohm1/speech-colab-hub/blob/main/notebooks/tts/indextts2_5.ipynb) |

## 在 Colab 打开

点击表格中的 **Open in Colab**，选择 GPU 运行时后按顺序执行。IndexTTS-2.5 需要 Python 3.10–3.11，当前 Colab 托管运行时不提供这一版本，须连接兼容的 GPU 本地运行时。若 Colab 的 GitHub 入口暂时无法加载，也可从 GitHub 下载对应 Notebook，在 Colab 选择 **File → Upload notebook** 打开副本。

## 使用与证据

打开 Notebook，选择 GPU 运行时，按顺序执行各单元并上传音频或输入文本。依赖会在 Colab 中安装，模型下载到显式指定的临时目录。不要在 Notebook 中填写访问令牌。运行成功后记录输出、单次耗时、显存与版本；未经 GPU 实测的条目保持 `unverified`。模板与生成、静态检查方式见 [设计说明](DESIGN.md)。
