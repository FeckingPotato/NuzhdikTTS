import requests
from random import randint

#здесь я просто скопировал код яндекса, который я подправил, и переделал в код для получения юморесок 

async def getJoke(token):
    url = 'https://api.vk.com/method/wall.get'

    data = {
        'access_token': token,
        'v': '5.124',
        'owner_id': '-92876084'
    }

    with requests.post(url, data=data, stream=True) as resp:
        if resp.status_code != 200:
            raise RuntimeError("Invalid response received: code: %d, message: %s" % (resp.status_code, resp.text))
        post_count = int(resp.json()['response']['count'])

    acceptable_joke = False
    while not acceptable_joke: #здесь перебираем посты, пока не найдём нужный
        random_post_id = randint(0, post_count-1) #если поставить параметр offset равный количеству постов, то вк выдаст пустой ответ
        data['offset'] = random_post_id
        with requests.post(url, data=data, stream=True) as resp:
            if resp.status_code != 200:
                raise RuntimeError("Invalid response received: code: %d, message: %s" % (resp.status_code, resp.text))
            joke = resp.json()['response']['items'][0]
            if ('attachments' not in joke) and (len(joke['text']) < 5000): #прикреплённые файлы могут влиять на смысл шутки, а tts яндекса не даёт озвучивать текст длиной более 5000 символов
                acceptable_joke = joke['text']
    return acceptable_joke