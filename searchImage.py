import cv2
import face_recognition
import csv
import json
import urllib.request
import numpy
import time

with open("sample.json", "r+") as file:
    file_data = json.load(file)
    print(len(file_data['data']))
def update(url,name,id):
    response = urllib.request.urlopen(url)
    imgCheck = face_recognition.load_image_file(response)
    imgCheck = cv2.cvtColor(imgCheck, cv2.COLOR_BGR2RGB)
    encodeCheck = face_recognition.face_encodings(imgCheck)[0]
    dictionary = {
        "name": name,
        "data": encodeCheck.tolist(),
        "id": id,
    }
    with open("sample.json", "r+") as file:
        file_data = json.load(file)
        for i,item in enumerate(file_data["data"]):
            if item['id'] == id:
                file_data["data"][i] = dictionary
                break
        file.seek(0)
        json.dump(file_data, file, indent=4)
# update("http://localhost:3000/pic/biden.jpg","obama","1")
def delete(id):
    dictionary = {
        "name": '',
        "data": [],
        "id": id,
    }
    with open("sample.json", "r+") as file:
        file_data = json.load(file)
        for i, item in enumerate(file_data["data"]):
            if item['id'] == id:
                file_data["data"][i] = dictionary
                break
        file.seek(0)
        json.dump(file_data, file, indent=4)
# delete('1')
def writer_file_json(url,name,id):
    response = urllib.request.urlopen(url)
    imgCheck = face_recognition.load_image_file(response)
    imgCheck = cv2.cvtColor(imgCheck, cv2.COLOR_BGR2RGB)
    encodeCheck = face_recognition.face_encodings(imgCheck)[0]
    dictionary = {
        "name": name,
        "data": encodeCheck.tolist(),
        "id": id,
    }
    with open("sample.json", "r+") as file:
        file_data = json.load(file)
        file_data["data"].append(dictionary)
        file.seek(0)
        json.dump(file_data, file, indent=4)

# writer_file_json("http://localhost:3000/pic/obama3.jpg","obama3","4")

def search_image(url):
    response = urllib.request.urlopen(url)
    imgCheck = face_recognition.load_image_file(response)
    imgCheck = cv2.cvtColor(imgCheck, cv2.COLOR_BGR2RGB)
    encodeCheck = face_recognition.face_encodings(imgCheck)[0]
    my_list = []
    # start_time = time.time()
    with open('sample.json', 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)
        for line in json_object['data']:
            arr = numpy.array(line['data'])
            results = face_recognition.compare_faces([arr], encodeCheck)
            if results[0] == True:
                faceDis = face_recognition.face_distance([arr], encodeCheck)
                my_list.append({'data': faceDis[0], 'name': line['name'], 'id': line['id']})
        # print(my_list)
    return my_list
    # end_time = time.time()
    # print("thơi gian 1: ", end_time - start_time)
# data = search_image("http://localhost:3000/32bit.png")
# print(data)
