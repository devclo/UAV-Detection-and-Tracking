import whisper
from moviepy.editor import VideoFileClip

def extract_audio(video_path):
    video_clip = VideoFileClip(video_path)
    audio_path = video_path + ".wav"
    video_clip.audio.write_audiofile(audio_path)
    return audio_path

def transcribe_audio(whisper_model, audio_path):
    result = whisper_model.transcribe(audio_path)
    return result["text"]

