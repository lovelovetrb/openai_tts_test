import os
import random

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.environ["OPENAI_API_KEY"]
client = OpenAI(api_key=api_key)

# textファイルを読み込み、1行づつリストに格納
speech_text_file = open("./speech_text.txt", "r")
speech_text_list = speech_text_file.readlines()

for i, text in enumerate(speech_text_list):
    speech_file_path = f"./out/{i}.mp3"
    print(f"Create {speech_file_path}")
    print(text)
    voice_list = ["alloy", "echo", "fable", "onyx", "nova", "shimmer"]
    voice = random.choice(voice_list)
    response = client.audio.speech.create(
        model="tts-1",
        voice=voice,
        input=text,
    )
    response.stream_to_file(speech_file_path)

print("Finish!")
