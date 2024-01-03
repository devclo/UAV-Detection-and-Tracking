from video_processing import download_video
from audio_transcription import extract_audio, transcribe_audio
import whisper

def transcribe_video_from_url(video_url):
    video_path = download_video(video_url)
    print(f"Downloaded video path: {video_path}")

    audio_path = extract_audio(video_path)
    print(f"Extracted audio path: {audio_path}")

    model = whisper.load_model("base")
    transcription = transcribe_audio(model, audio_path)
    print(f"Transcription: {transcription}")

    os.remove(audio_path)

if __name__ == "__main__":
    input_url = 'https://youtu.be/DhmZ6W1UAv4'
    transcribe_video_from_url(input_url)
