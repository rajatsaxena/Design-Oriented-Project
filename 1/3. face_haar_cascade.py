import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
nose_cascade = cv2.CascadeClassifier('haarcascade_mcs_nose.xml')
mouth_cascade = cv2.CascadeClassifier('Mouth.xml')

cap = cv2.VideoCapture('cam3.mp4')

while(cap.isOpened()):
	ret, img = cap.read() 
	gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
	faces = face_cascade.detectMultiScale(gray_img, 1.05, 5)
	#print faces

	for (p,q,r,s) in faces:
		cv2.rectangle(img,(p,q),(p+r,q+s),(255,0,0),2)
		face_gray = gray_img[q:q+s, p:p+r] 
		face_color = img[q:q+s, p:p+r] 
		
		eyes = eye_cascade.detectMultiScale(face_gray) 
	 	for (ep,eq,er,es) in eyes:
			cv2.rectangle(face_color,(ep,eq),(ep+er,eq+es), (0,255,0),2)
		
	cv2.imshow("output", img)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
