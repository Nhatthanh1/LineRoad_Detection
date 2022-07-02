import cv2 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import os
from matplotlib.colors import hsv_to_rgb

video= cv2.VideoCapture('line.mp4')
while True:
    ret,frame = video.read()
    if not ret:
        video= cv2.VideoCapture('line.mp4')
        continue
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    # define range of yellow color in HSV
    lower_yellow = (0, 150, 100)
    upper_yellow = (49, 255, 255)
    # Threshold 
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    # Bitwise-AND mask and original image
    blur = cv2.GaussianBlur(mask, (7, 7), 0)
    edges = cv2.Canny(mask, 75, 150, apertureSize=3)
    lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi/180, threshold=100)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
    cv2.imshow("frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
video.release()
cv2.destroyAllWindows()