import cv2
import numpy as np
import os
import shutil

def pupil_detect(eyeArr):
    rows, cols, _ = eyeArr.shape

    gray_eye = cv2.cvtColor(eyeArr, cv2.COLOR_BGR2GRAY)
    gray_eye = cv2.GaussianBlur(gray_eye, (9, 9), 0)
    gray_eye = cv2.medianBlur(gray_eye, 3)

    threshold = cv2.threshold(gray_eye, 25, 255, cv2.THRESH_BINARY_INV)[1]
    contours = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[1]
    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

    for cnt in contours:
        (x, y, w, h) = cv2.boundingRect(cnt)
        cv2.circle(eyeArr, (x + int(w/2), y + int(h/2)), int((h)/3), (0, 0, 255), 3)
        cv2.line(eyeArr, (x + int(w/2), 0), (x + int(w/2), rows), (0, 255, 0), 2)
        cv2.line(eyeArr, (0, y + int(h/2)), (cols , y + int(h/2)), (0, 255, 0), 2)
        break
    
    cv2.imwrite(out_dir + 'res_' + f, eyeArr)
    return eyeArr

input_dir = './samples/'
out_dir = './result/'


files = [file for file in os.listdir(input_dir) if file.endswith(".jpg")]

if os.path.exists(input_dir + "result") and os.path.isdir(input_dir + "result"):
    shutil.rmtree(input_dir + "result")
if not os.path.exists(input_dir + "result"):
    os.mkdir(input_dir + "result")
    
count = 1
for f in files:
    print("Processing file: ", f)
    pupil_detect(cv2.imread(input_dir + str(f)))
    count += 1
    print("----------Processing Done------------")