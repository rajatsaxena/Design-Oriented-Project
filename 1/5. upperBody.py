import cv2
import numpy as np

upper_body_cascade =  cv2.CascadeClassifier('haarcascade_upperbody.xml')

cap = cv2.VideoCapture('cam3.mp4')

while(cap.isOpened()):
	ret, img = cap.read() 
	gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
	upperBody = upper_body_cascade.detectMultiScale(gray_img, 1.05, 5)
       
        for (up,uq,ur,us) in upperBody:
		cv2.rectangle(img,(up,uq),(up+ur,uq+us),(0,255,0),2)
 
	cv2.imshow("output", img)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
