import cv2

def ComputeMask(frames):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    for frame in frames:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray)
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray)

    cv2.imshow('frame',frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

