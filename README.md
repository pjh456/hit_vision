# Hit Vision（移动端障碍物识别与语音提示）

这是一个面向安卓端的本地障碍物识别项目：使用 YOLO 进行目标检测，结合 ARCore Depth API 获取深度并估算米级距离，将检测到的障碍物与距离拼接成文本，交给本地 TTS 生成语音提示。

## 仓库定位

以 Python 端快速迭代与模型导出为主，最终部署到 Android 原生推理引擎（如 MNN）。

## 核心功能

- 目标检测：使用 Ultralytics YOLO 预训练模型进行障碍物识别。
- 深度/测距：Android 端使用 ARCore Depth API 生成深度图，估算真实距离（米级）。
- 语音提示：将检测结果拼接为文本，交由本地 TTS 生成语音。

## 技术栈

- 检测：Ultralytics YOLO（预训练权重）
- 深度：ARCore Depth API（Android）
- 推理：MNN Runtime（Android）
- 语音：KittenTTS 或 Qwen3‑TTS（本地）
- 研发语言：Python（PC 侧快速迭代/导出/验证）

## 部署/运行要求（概览）

- PC 侧（研发与模型导出）
  - Python 3.10+（建议）
  - 依赖见 `requirements.txt`
- Android 侧（原生部署）
  - Android Studio + NDK + CMake
  - ARCore SDK（Depth API）
  - MNN Runtime（推理引擎）

**说明**
- 本仓库仅提供工程骨架与依赖配置；模型权重与 Android 端工程需按阶段添加。
- 若需米级真实距离，优先使用 ARCore Depth API（部分设备不支持需做兼容处理）。

**预计研发流程**
1. 在 PC 端用 Python 先验证检测与文本拼接逻辑。
2. 导出 YOLO 模型为移动端可用格式（ONNX → MNN）。
3. Android 端接入 ARCore Depth API，完成深度测距。
4. 拼接障碍物信息并触发本地 TTS 语音提示。
