import os
import shutil
import moviepy.editor
import uuid


def merging_videos(files):
    
    clips = []
    for file in files:
        
        with open(f"temp/{file.filename}", "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        clips.append(moviepy.editor.VideoFileClip(f"temp/{file.filename}"))
    
    Mearged_video=moviepy.editor.concatenate_videoclips(clips) 
    
    video_path = "temp/video.mp4"

    Mearged_video.write_videofile(video_path, codec='libx264')

    Mearged_video.close()

    return video_path