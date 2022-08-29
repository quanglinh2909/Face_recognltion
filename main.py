import cv2
import face_recognition
import time

start_time = time.time()
imageElon = face_recognition.load_image_file("pic/obama.jpg")
imageElon = cv2.cvtColor(imageElon,cv2.COLOR_BGR2RGB)

imgCheck = face_recognition.load_image_file("pic/obama2.jpg")
imgCheck = cv2.cvtColor(imgCheck,cv2.COLOR_BGR2RGB)

# xác định vị trí khuôn mặt
faceLoc = face_recognition.face_locations(imageElon)[0]
# print(faceLoc)

# Mã hóa hình ảnh
encodeElon = face_recognition.face_encodings(imageElon)[0];
#vẽ hình chữ nhật
# cv2.rectangle(imageElon,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2)


# xác định vị trí khuôn mặt
faceCheck = face_recognition.face_locations(imgCheck)[0]
# print(faceCheck)

# Mã hóa hình ảnh
encodeCheck = face_recognition.face_encodings(imgCheck)[0];
#vẽ hình chữ nhật
# cv2.rectangle(imgCheck,(faceCheck[3],faceCheck[0]),(faceCheck[1],faceCheck[2]),(255,0,255),2)
end_time = time.time()
print("thơi gian 1: ",end_time - start_time)
#so sanh hai hình ảnh
results = face_recognition.compare_faces([encodeElon],encodeCheck)
print(results)

#khoản cách (sai số) của hai bức ảnh
faceDis = face_recognition.face_distance([encodeElon],encodeCheck)
print(results,faceDis)

# cv2.putText(imgCheck,f"{results}{1- round(faceDis[0],2)}",(50,50),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),2)
#
# cv2.imshow("Elon",imageElon)
# cv2.imshow("check",imgCheck)
#
# cv2.waitKey()
