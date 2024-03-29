import numpy as np
import cv2
import pickle
import os
from PIL import Image
import  pickle
import statistics
from statistics import mode

def recognizers():
    from . import pmenu
    face_cascade = cv2.CascadeClassifier(
        r'C:\Users\Pollam\Desktop\DBMS\Police\cascades\data\haarcascade_frontalface_alt2.xml')

    os.chdir(r'C:\Users\Pollam\Desktop\DBMS\Police')
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("recognizers/trainner.yml")
    labels = {"person_name": 1}
    with open("pickles/labels.pickle", 'rb') as f:
        og_labels = pickle.load(f)
        labels = {v: k for k, v in og_labels.items()}
    cap = cv2.VideoCapture(0)
    l=[]
    while (True):

        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
        for (x, y, w, h) in faces:
            print(x,y,w,h)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]
            id_, conf = recognizer.predict(roi_gray)
            if conf >= 50 and conf <= 80:
                font = cv2.FONT_HERSHEY_SIMPLEX
                name = labels[id_]
                color = (255, 255, 255)
                stroke = 2
                cv2.putText(frame, name, (x, y), font, 1, color, stroke, cv2.LINE_AA)
                l.append(name)
            color = (255, 0, 0)
            stroke = 2
            end_cord_x = x + w
            end_cord_y = y + h
            cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)
        cv2.imshow('frame', frame)
        if cv2.waitKey(20) & 0xFF == ord('q') or len(l)>=31:
            print(mode(l))
            break
    cap.release()
    cv2.destroyAllWindows()
    pmenu.gui()
    return