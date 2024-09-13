import os
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from functions.audio_track import audio_track
from functions.merging_videos import merging_videos

app = FastAPI()


@app.get("/")
async def read_root():

    return {"test"}


@app.post("/audio_track/")
async def create_audio(file: UploadFile):

    if file.content_type == "video/mp4":

        root, ext = os.path.splitext(file.filename)
        return FileResponse(path=audio_track(file), filename=f'{root}_audio.mp3', media_type='multipart/form-data')

    else:
        
        return {"Загрузите пожалуйста файл .mp4"}


@app.post("/merging_videos/")
async def create_video(files: list[UploadFile]):

    for file in files:
        if file.content_type != "video/mp4":
            return {"Загрузите пожалуйста файл .mp4"}
    
    return FileResponse(path=merging_videos(files), filename='video.mp4', media_type='multipart/form-data')


