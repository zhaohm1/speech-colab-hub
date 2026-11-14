# 语音模型 Colab Hub 设计

## 研究问题与边界

目标是让研究人员用少量步骤在 Colab 上完成开源 ASR/TTS 模型的单样本推理，并留存可追溯的运行条件。首阶段只实现 Whisper ASR；TTS 提供模板，不声称已有模型通过推理。单样本输出与耗时不代表准确率或稳定性能。

## 参考仓库

[donvito/notebooks](https://github.com/donvito/notebooks) 将 Notebook 放在 `colab/`，README 按任务列出功能、运行设备、模型卡与 Colab 按钮。其 [LFM3-Audio-2B 语音示例](https://github.com/donvito/notebooks/blob/main/colab/LFM3-Audio-2B-voice.ipynb) 依次安装依赖、检查 GPU、加载模型、准备样例、演示 ASR/TTS 并说明限制。本项目保留直接打开和顺序运行的体验，增加注册表、可重复生成、静态校验和验证状态。

## 模板与注册

ASR/TTS 共用顺序：介绍及来源；Colab GPU/磁盘检查；安装依赖；版本与设备记录；模型下载和加载；用户输入；推理与可查看输出；成功后的耗时/显存记录；限制与验证状态。ASR 使用上传音频，TTS 使用输入文本并试听音频。模型特有推理逻辑由模板中的任务段提供，不把核心模型代码复制进仓库。

`configs/models.yaml` 存放 ID、任务、官方来源、模型 revision、许可、依赖版本、Colab 路径、GPU 要求及验证状态。生成器只接受已登记模型，输出稳定的 Notebook。校验器检查注册、nbformat 结构、代码语法、无执行输出、README 链接和状态证据。所有生成文件可重建，手改应回填配置或模板。

## 验证依据

静态检查只支持格式、语法与链接一致性。`verified` 必须附 Colab GPU 真实运行日志，包含设备、依赖、模型版本、输入、成功输出、耗时和显存；无日志保持 `unverified`。若模型下载或推理失败，应保留失败记录，不推断性能。

## 目录

```text
speech-colab-hub/
├── README.md
├── DESIGN.md
├── AGENTS.md
├── configs/models.yaml
├── templates/asr.ipynb
├── templates/tts.ipynb
├── notebooks/asr/whisper.ipynb
├── scripts/generate_notebooks.py
├── scripts/validate_notebooks.py
└── validation/README.md
```
