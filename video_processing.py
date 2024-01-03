import os
import yt_dlp
from moviepy.editor import VideoFileClip

def sanitize_filename(filename):
    return "".join([c if c.isalnum() or c in " .-_" else "_" for c in filename])

def download_video(video_url, output_path='downloads'):
    if not os.path.isdir(output_path):
        os.makedirs(output_path)

    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'merge_output_format': 'mp4',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=True)
        filename = ydl.prepare_filename(info_dict)
        if not os.path.exists(filename):
            filename = sanitize_filename(filename)
            if not os.path.exists(filename):
                raise FileNotFoundError(f"The video file {filename} was not found. Download may have failed.")
        return filename
