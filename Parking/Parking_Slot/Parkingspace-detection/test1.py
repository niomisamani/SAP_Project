import cv2
import numpy as np


cap = cv2.VideoCapture("easy1.mp4")

def draw(event,x,y,flags,param):
    if event==cv2.Event_LBUTTONDOWN:
        print(x,y)

while True:
    ret, frame = cap.read()
    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue
    frame=cv2.resize(frame,(1020,500))

    cv2.imshow('FRAME', frame)
    cv2.setMouseCallback('FRAME',draw)

    Key = cv2.waitKey(100) & 0xFF
cap.release()
cv2.destroyAllWindows()
