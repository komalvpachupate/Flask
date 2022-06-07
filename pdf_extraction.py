import pytesseract
from pdf2image import convert_from_path
import cv2
import os


pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
tessdata_dir_config = '--tessdata-dir "C:\\Program Files\\Tesseract-OCR\\tessdata"'

# converts pdf to list of images
def pdf_to_img(pdf):
    pdf_pages = convert_from_path(pdf, dpi=350, poppler_path=r'C:\Program Files\poppler-0.68.0\bin')
    i = 1
    img_list = []
    for page in pdf_pages:
        page.save('pdf_images/page' + str(i) + '.jpg', 'JPEG')
        img_list.append('page' + str(i) + '.jpg')
#         print('img_list',img_list)
        i += 1
    print('PDF to Image Conversion Successful!')
    return img_list

# text is extracted from each contours stored
def extract_text(img_list):
#     print('bbb', boxes)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text = ''
    for key in img_list:
#         print("kkk", key)
        img = cv2.imread('pdf_images/'+ key)
        for x, y, w, h in img_list[key]:
            cropped_image = img[y:y + h, x:x + w]
            _, thresh = cv2.threshold(cropped_image, 127, 255, cv2.THRESH_BINARY)
            text += str(pytesseract.image_to_string(thresh, config=tessdata_dir_config))
    print('Text Extraction Completed!')
    return text

# base function
def ocr(filename, show_boxes):
    if filename:
        img_list = pdf_to_img(filename)
        # print(img_list)
        # boxes = bounding_boxes(img_list, show_boxes)
        # if not show_boxes:
        text = extract_text(img_list)
        # text = 'hii'
        return text
    # else:
    #     st.warning('Please select a PDF file!')

filename = "static\pdfs\EB-51-Quality-of-Indian-Wheat.pdf"

a = ocr(filename, 0)