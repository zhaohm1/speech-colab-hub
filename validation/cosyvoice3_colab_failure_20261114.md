# CosyVoice3 Colab 运行失败记录

- 用户提供运行后 Notebook；原始文件 SHA-256：`ace174e1b7f8aea452c0f35328f38fd6018ec3a5bb20e46c593ce96fc303e3ad`。原始 Notebook 未上传公开仓库。
- Colab Tesla T4（15360 MiB），Python 3.13.16，torch 2.14.1+cu130，torchaudio 2.11.0+cu130。依赖安装、源码检出和 ModelScope 下载单元均返回 0；源码 commit `074ca6dc9e80a2f424f1f74b48bdd7d3fea531cc`。
- 第 5 个代码单元在 `llm.pt` SHA-256 校验处失败。后续环境导入、模型加载和合成单元均未执行；因此 Colab 推理仍为 `unverified`。用户文件未记录下载文件的实际 SHA-256。
- 原因：Notebook 请求 ModelScope revision `3a9eb0e104c9ce5bb7ef0af4ac86d9b79abc4029`，却使用了较新 revision `2c1f17328e4c6885cfe24bf0581e305c4377195f` 中 `llm.pt` 的哈希 `69f43bd…`。ModelScope 官方文件清单显示固定 revision 的 `llm.pt` 大小 2,024,669,130 bytes、SHA-256 `d9565e41…`；`llm.rl.pt` 和 `speech_tokenizer_v3.batch.onnx` 不在该 revision 中。校验表已按固定 revision 修正；此修正尚未经重新运行验证。
