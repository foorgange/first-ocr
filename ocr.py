from PIL import Image
import pytesseract


# 如果不是全局安装了tesseract，而是安装在特定路径下，需要指定路径
# pytesseract.pytesseract.tesseract_cmd = r'<完整路径>\tesseract.exe'

# 打开一个图像文件
img = Image.open('ocr.png')

# 使用Tesseract进行OCR处理
text = pytesseract.image_to_string(img, lang='chi_sim', config='--psm 6')
print("Recognized text:", text.encode('utf-8').decode('utf-8'))


# 输出识别的文字
print(text)
