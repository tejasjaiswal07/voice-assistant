# text_to_speech.py
from gtts import gTTS
import os

def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    os.system("start response.mp3")  # On Windows
    # os.system("afplay response.mp3")  # On macOS
    # os.system("mpg321 response.mp3")  # On Linux