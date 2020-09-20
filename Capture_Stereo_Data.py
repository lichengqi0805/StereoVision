import cv2
import numpy as np
import os

cap_1 = cv2.VideoCapture(1)
cap_2 = cv2.VideoCapture(0)
index = 1
while True:
    ret_1, frame_1 = cap_1.read()
    ret_2, frame_2 = cap_2.read()
    cv2.imshow("CAM 1", frame_1)
    cv2.imshow("CAM 2", frame_2)
    input = cv2.waitKey(1) & 0xFF
    if input == ord('x'):
        cv2.imwrite("124/cam_1 %d.jpeg" % (index), frame_1)
        print("Picture taken %d" % (index))
        cv2.imwrite("124/cam_2 %d.jpeg" % (index), frame_2)
        index += 1
    if input == ord('q'):
        break