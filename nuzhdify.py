from pydub import AudioSegment
from math import ceil

async def nuzhdify():
    theme = []
    theme.append(AudioSegment.from_ogg('./input_sound/theme1.ogg') - 4) #собираем нужные аудиофайлы, -4 надо, чтобы тема нуждиков была не слишком громкой
    theme.append(AudioSegment.from_ogg('./input_sound/theme2.ogg') - 4)
    tts_setup = AudioSegment.from_ogg('./input_sound/tts_setup.ogg')
    tts_punchline = AudioSegment.from_ogg('./input_sound/tts_punchline.ogg')
    ha = AudioSegment.from_ogg('./input_sound/ha.ogg')

    setup_length = ceil(len(tts_setup)/len(theme[0])) #измеряем длину сетапа
    
    i = 0
    k = 0
    theme_final = AudioSegment.empty()
    while i < setup_length: #удлиняем тему
        theme_final += theme[k]
        k = int(not k)
        i += 1

    result = theme_final.overlay(tts_setup) #соединяем всё это
    result += AudioSegment.silent(duration=300) #300 мс тишины нужны, чтобы разделять сетап и панчлайн
    result += tts_punchline
    result += ha

    result.export('./output_sound/result.ogg', format='ogg')
    return 'result.ogg'