import re
#короче, тут какие-то алгоритмы, которые я писал в 2 часа ночи, они вроде работают, но не знаю как
def joinSetup(separated, original_text):
    result = []
    result.append(separated[-1])
    separated.pop(-1)
    result.append(' '.join(separated))
    result.reverse()
    result[0] = original_text.replace(result[1], '')
    return result

def joinSetupComma(separated, original_text):
    result = []
    result.append(separated[-1])
    result.append(' '.join(separated))

def dialog_separate(text, regex):
    text_for_split = re.sub(regex, '/|/FuCK/|/', text) #сделал костыль, так как либо я дебил, либо деление строки при помощи регулярных выражений работает криво
    text_split = list(filter(None, text_for_split.split('/|/FuCK/|/')))
    text_split_newline = list(filter(None, text.split('\n')))
    if len(text_split) == len(text_split_newline):
        result = text_split
        return result
    else:
        return False

def separate(text):
    text = text.replace('"', '')
    if re.match(r'[-—–−]', text): #проверяем все возможные варианты диалогов с горизонтальной палкой, панчлайном считаем последнее высказывание
        separated = dialog_separate(text, r'(^\s*-)|(\ns*-)')
        if (separated):
            return joinSetup(separated, text)
        separated = dialog_separate(text, r'(^\s*—)|(\ns*—)')
        if (separated):
            return joinSetup(separated, text)
        separated = dialog_separate(text, r'(^\s*–)|(\ns*–)')
        if (separated):
            return joinSetup(separated, text)
        separated = dialog_separate(text, r'(^\s*−)|(\ns*−)')
        if (separated):
            return joinSetup(separated, text)
    if re.search(r'[.!?]\s*\S+', text): #проверяем наличие нормального текста с предложениями, панчлайном считаем последнее предложение
        separated = list(filter(None, re.split(r'[.!?]', text)))
        return joinSetup(separated, text)
    if ',' in text: #проверяем наличие запятых в тексте без предложений, панчлайном считаем то, что идёт после последней запятой
        separated = list(filter(None, text.split(',')))
        return joinSetup(separated, text)
    if len(re.findall(r'[-—–−]', text)) == 1: #если шутка имеет только одно тире/дефис/минус, то панчлайном считаем то, что идёт после знака препинания
        separated = list(filter(None, re.split(r'[-—–−]', text)))
        return joinSetup(separated, text)
    if '\n' in text: #если шутка делится только абзацами, то панчлайном считаем последний абзац
        separated = list(filter(None, text.split('\n')))
        return joinSetup(separated, text)
    separated = list(filter(None, text.split(' '))) #если всё очень плохо, то панчлайном считаем последнее слово
    return joinSetup(separated, text)