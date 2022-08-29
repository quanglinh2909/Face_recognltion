import csv
import cv2
import face_recognition
import numpy as np
import time
import urllib.request
start_time = time.time()

response = urllib.request.urlopen('http://localhost:3000/32bit.png')

imgCheck = face_recognition.load_image_file(response)
imgCheck = cv2.cvtColor(imgCheck,cv2.COLOR_BGR2RGB)

encodeCheck = face_recognition.face_encodings(imgCheck)[0];
# faceDis = face_recognition.face_distance([encodeCheck], encodeCheck)
# print(encodeCheck)

with open('example.csv', 'r+') as file:
   myList = file.readlines();
   print(len(myList))

   for line in myList:
       a = np.fromstring(line, dtype=float, sep=',')
       faceDis = face_recognition.face_distance([a], encodeCheck)
       print(faceDis)
end_time = time.time()
print("thơi gian 1: ",end_time - start_time)
