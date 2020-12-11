import requests

#здесь я просто скопировал код яндекса и чуток подправил, за объяснениями сюда: https://cloud.yandex.ru/docs/speechkit/tts/request

async def getTts(text, token):
    url = 'https://tts.api.cloud.yandex.net/speech/v1/tts:synthesize'
    headers = {
        'Authorization': 'Bearer ' + token,
    }

    data = {
        'text': text,
        'voice': 'filipp',
        'folderId': 'b1gapu1ptvd2lnf676oh'
    }

    with requests.post(url, headers=headers, data=data, stream=True) as resp:
        if resp.status_code != 200:
            raise RuntimeError("Invalid response received: code: %d, message: %s" % (resp.status_code, resp.text))
        return resp.content
