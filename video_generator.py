import os
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, AudioFileClip
import requests
from gtts import gTTS

def download_stock_footage(url):
    response = requests.get(url)
    with open('stock_video.mp4', 'wb') as f:
        f.write(response.content)

def add_text_overlay(video_clip, text):
    txt_clip = (TextClip(text,fontsize=70,color='white')
                 .set_position('center')
                 .set_duration(video_clip.duration)
                 .crossfadein(1))
    return CompositeVideoClip([video_clip, txt_clip])

def generate_voice_over(text, output_file):
    tts = gTTS(text, lang='tr')
    tts.save(output_file)

def create_video(output_file):
    video_clip = VideoFileClip('stock_video.mp4')
    video_clip = video_clip.resize(height=1080).crop(width=1080, height=1920)

    text = "Felsefi düşüncelerle dolu bir yolculuk"
    video_with_text = add_text_overlay(video_clip, text)

    generate_voice_over(text, 'voice_over.mp3')
    audio_clip = AudioFileClip('voice_over.mp3')

    final_video = video_with_text.set_audio(audio_clip)
    final_video.write_videofile(output_file, codec='libx264')

if __name__ == "__main__":
    stock_video_url = 'URL_TO_STOCK_FOOTAGE'
    download_stock_footage(stock_video_url)
    create_video('final_video.mp4')
