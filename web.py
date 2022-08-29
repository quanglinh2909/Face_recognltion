from flask import Flask,jsonify,request
from flask_cors import CORS,cross_origin
import searchImage
app = Flask(__name__)

CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

@app.route("/",methods=["GET"])
@cross_origin(origins="*")
def home():
    return "home"

@app.route("/search",methods=["POST"])
@cross_origin(origins="*")
def search_image():
    request_json = request.json
    url = request_json['url']
    if(url is None):
        return "vui long nhap url"
    return searchImage.search_image(request_json['url'])


if __name__ == "__main__":
    app.run(host="localhost",port=3100)

