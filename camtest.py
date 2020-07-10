import numpy as np
import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
while(True):

    ret, frame = cap.read()
    if ret == False:
    	continue
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces=face_cascade.detectMultiScale(gray,1.3,5)
    # Display the resulting frame
    
    # cv2.imshow('Gray',gray)

    for (x,y,w,h) in faces:
    	cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),2)

    cv2.imshow('Frame',frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()