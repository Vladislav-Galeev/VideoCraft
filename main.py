import os
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from functions.audio_track import audio_track


app = FastAPI()


@app.get("/")
async def read_root():

    return {"test"}


@app.post("/audio_track/")
async def create_upload_file(file: UploadFile):

    if file.content_type == "video/mp4":
        
        root, ext = os.path.splitext(file.filename)
        return FileResponse(path=audio_track(file), filename=f'{root}_audio.mp3', media_type='multipart/form-data')

    else:
        
        return {"Загрузите пожалуйста файл .mp4"}