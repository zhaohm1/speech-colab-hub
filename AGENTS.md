# Hub 接入规范

- 先读 `DESIGN.md` 和 `configs/models.yaml`。每个新模型先核实官方代码、模型版本或 revision、许可、硬件和依赖，再登记；优先官方推理接口，不修改核心模型代码。
- 模型下载必须有明确目录。Colab 使用 `/content/models/<model>` 或用户明确指定的 Drive 子目录；本地研究下载遵循 `/mnt/e/models`。不得把权重写入仓库、默认用户缓存或 Codex 目录。记录实际来源、revision、路径、许可和可获得的 SHA-256。
- ASR 提供音频上传与文本结果；TTS 提供文本输入与音频试听。保留 GPU 检测、可重复依赖安装、运行环境与依赖版本、成功后同步计时和显存记录。单次推理不能写成准确率或稳定性能。
- 不在代码、输出或日志中保存凭证。需要认证时使用 Colab Secrets 或运行时交互输入，并在提交前清除执行输出。
- 修改注册表或模板后运行 `python scripts/generate_notebooks.py`，再运行 `python scripts/generate_notebooks.py --check` 和 `python scripts/validate_notebooks.py`。生成文件改动须能重建。
- 没有实际 Colab GPU 日志时状态保持 `unverified`。只有日志包含 GPU、模型与依赖版本、输入、成功输出、耗时和显存，才可登记 `verification_log` 并改为 `verified`。失败记录保留；静态检查不能充当 GPU 实测。
- README 为每个已登记模型提供任务、运行环境、来源、状态、Notebook 相对链接和 Open in Colab 链接。每阶段检查通过再提交 Git，提交范围只包含本 Hub。
