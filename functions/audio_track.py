import os
import shutil
import moviepy.editor
import uuid


def audio_track(file):

    file.filename = f"{uuid.uuid4().hex}.mp4"
    root, ext = os.path.splitext(file.filename)

    with open(f"temp/{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Путь к сохраненному видео
    video_path = f"temp/{file.filename}"
    # Путь к сохраненному аудио
    audio_path = f"temp/{root}.mp3"

    # Извлечение аудио с помощью MoviePy
    video_clip = moviepy.editor.VideoFileClip(video_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(audio_path)

    video_clip.close()
    audio_clip.close()

    return audio_path