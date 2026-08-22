# first-ocr

基于 **Tesseract** 和 **Pillow** 的简易 OCR 文字识别 Demo，用于学习 OCR 基础流程。

## 功能

- 读取本地图片，通过 Tesseract 引擎识别其中的文字
- 使用简体中文语言包（`chi_sim`），适合中英文混排的简单图片

## 环境要求

- Python 3.x
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) 引擎，并安装简体中文语言包（`chi_sim`）

  若 Tesseract 未安装在系统 PATH 中，可在 `ocr.py` 中指定完整路径：

  ```python
  pytesseract.pytesseract.tesseract_cmd = r'<完整路径>\tesseract.exe'
  ```

- Python 依赖：

  ```bash
  pip install pillow pytesseract
  ```

## 使用方法

1. 将待识别的图片命名为 `ocr.png`，放在 `ocr.py` 同目录下
2. 运行脚本：

   ```bash
   python ocr.py
   ```

3. 识别结果将输出到终端

## 文件结构

```text
first-ocr/
├── ocr.py     # OCR 识别脚本
└── ocr.png    # 示例识别图片
```
