import cv2
import face_recognition
import time
import csv
imgCheck = face_recognition.load_image_file("pic/32bit.png")
imgCheck = cv2.cvtColor(imgCheck,cv2.COLOR_BGR2RGB)

encodeCheck = face_recognition.face_encodings(imgCheck)[0];

with open('example.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(encodeCheck)