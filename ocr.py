import sys
import os
import time
from PIL import Image
import pytesseract
import cv2


def _preprocess(image_file, preprocess):
    if not preprocess:
        return image_file
    # load the image and convert it to grayscale
    image = cv2.imread(image_file)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # check to see if we should apply thresholding to preprocess the image
    if preprocess == "thresh":
        gray = cv2.threshold(gray, 0, 255,
                             cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    # make a check to see if median blurring should be done to remove noise
    elif preprocess == "blur":
        gray = cv2.medianBlur(gray, 3)
    else:
        raise "unknown preprocess option"
    # write the grayscale image to disk as a temporary file so we can
    # apply OCR to it
    filename = f"{os.getpid()}-{str(time.time()).replace('.','')}.png"
    cv2.imwrite(filename, gray)
    return filename


def ocr(image, preprocess=None, lang=None):
    filename = _preprocess(image, preprocess)
    text = pytesseract.image_to_string(Image.open(filename), lang=lang)
    if preprocess:
        os.remove(filename)
    return text
