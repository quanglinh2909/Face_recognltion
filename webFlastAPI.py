from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import searchImage
import time

class MyItem(BaseModel):
    url:str
class IsertItem(BaseModel):
    url:str
    name:str
    id:str

app = FastAPI()

@app.get("/")
async def home():
    return "day la hom"

@app.post("/search")
async def search_image(item:MyItem):
    try:
        start_time = time.time()

        data =  searchImage.search_image(item.url)
        end_time = time.time()
        print("thơi gian 1: ", end_time - start_time)
        return data

    except:
        return("sai duong dan")
@app.post("/insert")
async def insert_image(item:IsertItem):
    try:
        start_time = time.time()
        data =  searchImage.writer_file_json(item.url,item.name,item.id)
        end_time = time.time()
        print("thơi gian 1: ", end_time - start_time)
        return data
    except:
        return("sai duong dan")

if __name__ == "__main__":
    config = uvicorn.Config("webFlastAPI:app", port=5000, log_level="info")
    server = uvicorn.Server(config)
    server.run()
