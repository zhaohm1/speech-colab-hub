# Whisper Colab GPU 单样本验证记录

- 收到运行后 Notebook：2026-11-14；Notebook 内未记录实际运行时间。
- 原始运行文件：用户提供的 `whisper.ipynb`，仅保留在用户本地；SHA-256 `2f2e73db5a93770d3e27ec1cd23e418f60ab0d4c3f280eefc6122628e3e2f6db`。原始音频及完整运行后 Notebook 未发布。
- 执行顺序：代码单元 execution_count 为 1、2、3、4、5；无错误输出。
- 环境：Tesla T4，显存 15360 MiB；驱动 580.82.07；Python 3.13.16；Linux 6.6.159+ x86_64；CUDA 13.0；torch 2.14.1+cu130；openai-whisper 20250625；soundfile 0.14.0。
- 模型：Whisper `small`，官方 `whisper.load_model(..., device='cuda', download_root='/content/models/whisper')` 加载成功；日志显示下载 461 MiB。运行日志未给出权重文件 SHA-256；官方加载器执行下载校验，但本记录不声称独立文件哈希复核。
- 输入：用户上传单条 WAV，350720 bytes；原始文件名 SHA-256 `71480722e7156a7d322f41ae152b8d580070ffd23b20fd932c1cbbae646afff1`，文件名与音频内容未公开。
- 输出：转写非空，语言 `en`；转写文本 SHA-256 `c89fe423b2b6658ae74339d5d7508773ac74975bd1750c2129e7a8fd9f31d367`，字符数 123。公开记录不含原文；完整文本可在上述原始 Notebook 中核对。
- 单次耗时：4.03 s。计时包含该次 `model.transcribe` 的音频解码、预处理、推理与文本后处理，不包含模型加载与上传；调用前后有 CUDA 同步。
- CUDA 峰值 allocated：1066.7 MiB；峰值 reserved：1494.0 MiB；调用前 reserved：1494.0 MiB。峰值是当前 CUDA 进程统计，不能解释为该次推理的增量显存，也不是设备总体占用。
- CER/WER：待测；没有参考转写。仅支持该 Colab T4 环境、该输入上的单样本功能通过，不代表稳定延迟、准确率评测或其他 GPU 适配。
