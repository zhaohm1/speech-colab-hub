# 开源语音模型 Google Colab Notebook Hub

用 Google Colab 快速体验开源 ASR/TTS 模型的单样本推理。Notebook 保留模型来源、依赖与环境记录；单次体验不代表准确率或稳定性能评测。私有仓库使用者需要相应 GitHub 访问权限。

## ASR

| 模型 | 功能 | 运行环境 | 来源 | 验证状态 | Notebook | Colab |
| --- | --- | --- | --- | --- | --- | --- |
| Whisper small | 上传音频并转写 | Colab GPU，推荐 T4 | [官方代码](https://github.com/openai/whisper)、[模型说明](https://github.com/openai/whisper#available-models-and-languages)；MIT | `unverified`：尚无 Colab GPU 运行日志 | [查看 Notebook](notebooks/asr/whisper.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zhaohm1/speech-colab-hub/blob/main/notebooks/asr/whisper.ipynb) |

## TTS

TTS 模板已准备，首阶段尚无注册模型或可运行 Notebook。

## 私有仓库如何在 Colab 打开

**私有仓库推荐入口：**用有仓库权限的 GitHub 账号下载 [`notebooks/asr/whisper.ipynb`](notebooks/asr/whisper.ipynb)，在 Colab 选择 **File → Upload notebook** 打开副本。无需向 Colab 授予整个私有仓库的访问权限。

如需直接使用 Open in Colab 按钮，先在 [Colab 的 GitHub 打开页面](https://colab.research.google.com/github/) 勾选 **Include private repos**，按提示授权 GitHub。若仍看不到仓库或遇到 GitHub API `404`，核对授权时登录的 GitHub 账号及授权范围；不要反复重试按钮，改用上述上传方式。不要把访问令牌写进 Notebook。

## 使用与证据

打开 Notebook，选择 GPU 运行时，按顺序执行各单元并上传音频或输入文本。依赖会在 Colab 中安装，模型下载到显式指定的临时目录。不要在 Notebook 中填写访问令牌。运行成功后记录输出、单次耗时、显存与版本；未经 GPU 实测的条目保持 `unverified`。模板与生成、静态检查方式见 [设计说明](DESIGN.md)。
