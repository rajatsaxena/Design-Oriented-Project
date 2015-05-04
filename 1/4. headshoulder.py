import cv2
import numpy as np

head_shoudler_cascade = cv2.CascadeClassifier('haarcascade_head_and_shoulder.xml')

cap = cv2.VideoCapture('cam3.mp4')

while(cap.isOpened()):
	ret, img = cap.read() 
	gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
	headShoulder = head_shoudler_cascade.detectMultiScale(gray_img, 1.05, 5)
	
	for (hsp,hsq,hsr,hss) in headShoulder:
		cv2.rectangle(img,(hsp,hsq),(hsp+hsr,hsq+hss),(0,0,255),2)
 
	cv2.imshow("output", img)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
