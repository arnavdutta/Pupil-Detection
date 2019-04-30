import cv2
import numpy as np

cap = cv2.VideoCapture('video.mp4')
out = cv2.VideoWriter('output.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 30, (500,450))

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        roi = frame[50:500, 300:800]
        rows, cols, _ = roi.shape
        gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        gray_roi = cv2.GaussianBlur(gray_roi, (11, 11), 0)
        gray_roi = cv2.medianBlur(gray_roi, 3)

        threshold = cv2.threshold(gray_roi, 15, 255, cv2.THRESH_BINARY_INV)[1]
        contours = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[1]
        contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

        for cnt in contours:
            (x, y, w, h) = cv2.boundingRect(cnt)
            cv2.circle(roi, (x + int(w/2), y + int(h/2)), int((h)/3), (0, 0, 255), 2)
            cv2.line(roi, (x + int(w/2), 0), (x + int(w/2), rows), (50, 200, 0), 1)
            cv2.line(roi, (0, y + int(h/2)), (cols , y + int(h/2)), (50, 200, 0), 1)
            cv2.putText(roi, text = '[Press Q to Exit]', org = (int(cols - 180), int(rows - 15)), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 0.6, color = (0, 0, 0))
            cv2.putText(threshold, text = '[Press Q to Exit]', org = (int(cols - 180), int(rows - 15)), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 0.6, color = (255, 255, 255))
            cv2.putText(gray_roi, text = '[Press Q to Exit]', org = (int(cols - 180), int(rows - 15)), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 0.6, color = (0, 0, 0))
            break
            
        cv2.imshow("roi", roi)
        # cv2.imshow('Threshold', threshold)
        # cv2.imshow('gray_roi', gray_roi)
        out.write(roi)
    else:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        
    if cv2.waitKey(15) & 0xFF == ord('q'): # Press 'Q' on the keyboard to exit the playback
        break
cap.release()
out.release()
cv2.destroyAllWindows()