#!/usr/bin/python3
from dotenv import load_dotenv
load_dotenv()

import asyncio
import subprocess
import os
from getJoke import getJoke
from separate import separate
from getTts import getTts
from nuzhdify import nuzhdify

async def main():
    yc = subprocess.Popen('yc iam create-token', shell=True, stdout=subprocess.PIPE) #мне было лень получать токен при помощи python, поэтому использую консоль яндекса
    yc_token = yc.stdout.read().decode("utf-8")
    yc_token = yc_token.split('\n' ) #это нужно, чтобы убрать символ новой строки и не включать в переменную информацию, которая может идти после токена 
    vk_token = os.getenv("VK_TOKEN")
    joke = "Меня зовут Сергей Есенин, но бандюги зовут меня жарить спирт." #await getJoke(vk_token)
    print(joke)
    joke_separated = separate(joke)
    print(joke_separated)
    tts_setup_file = open('./input_sound/tts_setup.ogg', 'wb')
    tts_punchline_file = open('./input_sound/tts_punchline.ogg', 'wb')

    tts_setup = await getTts(joke_separated[0], yc_token[0])
    tts_punchline = await getTts(joke_separated[1], yc_token[0])

    tts_setup_file.write(tts_setup)
    tts_punchline_file.write(tts_punchline)

    await nuzhdify()


asyncio.run(main())
