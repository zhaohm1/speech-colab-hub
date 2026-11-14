# CosyVoice3 Colab T4 单句推理记录

- 日期：2026-11-15（北京时间；Colab 日志时间为 UTC）。
- 运行入口：`notebooks/tts/cosyvoice3.ipynb`，Google Colab T4。实际运行中补齐依赖并采用半精度模型加载；相应修改已写回模板与生成的 Notebook。
- 设备与环境：Tesla T4 15360 MiB，驱动 580.82.07；Linux 6.6.159+，Python 3.13.16，torch 2.14.1+cu130，torchaudio 2.11.0+cu130，transformers 4.51.3，modelscope 1.40.3，onnxruntime-gpu 1.32.0，openai-whisper 20250625，lightning 2.6.6，pyworld 0.3.5，soundfile 0.14.0。
- 源码 commit：`074ca6dc9e80a2f424f1f74b48bdd7d3fea531cc`；模型 revision：`3a9eb0e104c9ce5bb7ef0af4ac86d9b79abc4029`；模型位于 Colab `/content/models/FunAudioLLM/Fun-CosyVoice3-0.5B-2512`。Notebook 中六个关键文件的 SHA-256 校验均返回 OK，包括先前失败的 `llm.pt`。
- 输入：`你好，欢迎体验 CosyVoice3。`；官方 `asset/zero_shot_prompt.wav`；指令 `You are a helpful assistant. 请用自然、清晰的语气朗读。<|endofprompt|>`；seed 1986；`inference_instruct2`、`stream=False`、`speed=1.0`、`text_frontend=True`。
- 成功输出：单声道 24 kHz PCM_16 WAV，65280 帧，2.72 秒，SHA-256 `d0e9da9f73d3f70b1bcf4ccd73cc0327071bd7a18aed451af48996f7c64268d8`。Colab 页面显示音频播放器，下载文件经本地 `wave` 与 SHA-256 复核。
- 单次调用耗时 10.251 秒，RTF 3.769；CUDA peak allocated 1708.2 MiB、peak reserved 2424.0 MiB。计时包含 `inference_instruct2` 与输出拼接，排除安装、下载、加载与 WAV 写入；无预热、仅一次输入，因此不代表稳定性能。
- 本地原始证据：`/home/zhaohm/deploy/experiments/exp001_cosyvoice3_tts/results/cosyvoice3_colab_t4_20261115_executed.ipynb`（SHA-256 `2848be2495f59f9573304685d38b4ee6ae378c54ea79dddc5b97bdb4f212790d`）及同目录 `cosyvoice3_colab_t4_20261115.wav`。带输出的 Notebook 保存在本地实验目录；公开仓库的 Notebook 不包含执行输出。

运行中保留的失败与限制：首次 `Run all` 时缺少 `lightning`，补齐后又缺少 `pyworld`；以默认 float32 构建模型时耗尽 12.67 GiB RAM，Colab 自动重启。尝试启用磁盘 swap 时 `swapon` 返回 255，交换文件已从临时运行时删除。随后在模型构建期间设置默认 dtype 为 float16，并调用官方 `AutoModel(..., fp16=True)`，加载及合成成功。下载 `llm.pt` 时曾有一次 `ConnectionError`，ModelScope 自动续传完成。上述过程不证明其他 Colab 配置或不同版本的适配，也不构成音质评测。
