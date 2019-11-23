import numpy as np
import cv2
import pickle
import os
from PIL import Image
import  pickle
import statistics
from statistics import mode

def trainer(name):
    face_cascade = cv2.CascadeClassifier(
        r'C:\Users\Pollam\Desktop\DBMS\Police\cascades\data\haarcascade_frontalface_alt2.xml')
    recognizer=cv2.face.LBPHFaceRecognizer_create()
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    image_dir = os.path.join(BASE_DIR, 'Staff')
    current_id=0
    x_train=[]
    y_labels=[]
    label_ids={}
    webcam(image_dir,name)
    image_dir2=os.path.join(image_dir,name)
    for root,dirs,files in os.walk(image_dir):
        for file in files:
            if file.endswith('png') or file.endswith('jpg'):
                path=os.path.join(root,file)
                label=os.path.basename(root).replace(" ","-").lower()
                print(label,path)
                if not label in label_ids:
                    label_ids[label]=current_id
                    current_id+=1
                id_=label_ids[label]
                print(label_ids)
                pil_image=Image.open(path).convert('L')
                image_array=np.array(pil_image,'uint8')
                print(image_array)
                faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.2, minNeighbors=5)
                for (x, y, w, h) in faces:
                    roi=image_array[y:y+h,x:x+w]
                    x_train.append(roi)
                    y_labels.append(id_)
    print(y_labels)
    print(x_train )
    os.chdir(r'C:\Users\Pollam\Desktop\DBMS\Police\pickles')
    with open("labels.pickle",'wb') as f:
        pickle.dump(label_ids,f)


    os.chdir(r'C:\Users\Pollam\Desktop\DBMS\Police\recognizers')
    recognizer.train(x_train, np.array(y_labels))
    recognizer.save("trainner.yml")

def webcam(image_dir,name):
    face_cascade = cv2.CascadeClassifier(
        r'C:\Users\Pollam\Desktop\DBMS\Police\cascades\data\haarcascade_frontalface_alt2.xml')
    cap = cv2.VideoCapture(0)

    pathu = image_dir + "\ " + name
    os.mkdir(pathu)
    os.chdir(pathu)
    i = 1
    while (True):

        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)

        for (x, y, w, h) in faces:
            roi_gray = gray[y:y + h, x:x + w]
            i += 1
            img_item = str(i)+".png"
            cv2.imwrite(img_item, roi_gray)
            color = (255, 0, 0)
            stroke = 2
            width = x + w
            height = y + h
            cv2.rectangle(frame, (x, y), (width, height), color, stroke)
        cv2.imshow('frame', frame)
        print(i)

        if cv2.waitKey(5) & 0xFF == ord('q') or i==100:
            break

    cap.release()


cv2.destroyAllWindows()