import requests
from pprint import pprint
from structure_example.config_data.config import YANDEX_DICT_KEY

API_KEY = YANDEX_DICT_KEY
BASE_URL = "https://dictionary.yandex.net/api/v1/dicservice.json"


def get_langs():
    response = requests.get(
        "{base_url}/getLangs".format(base_url=BASE_URL), params={"key": API_KEY}
    )
    return response

def lookup(lang, text, ui="ru"):
    response = requests.get(
        "{base_url}/lookup".format(base_url=BASE_URL),
        params={
            'key': API_KEY,
            'lang': lang,
            'text': text,
            'ui': ui,
        }
    )
    return response

langs_response = get_langs()
if langs_response.status_code != 200:
    print("Не удалось получить список направлений перевода")
    exit(1)

langs = langs_response.json()
print(langs)

# while (lang := input("Укажите направление перевода: ")) not in langs:
#     print('Неправильное направление.')

text = input('Текст для перевода: ')
lookup_response = lookup(lang='ru-en', text=text)
if lookup_response.status_code != 200:
    print("Перевод не удался для текста: ", lookup_response.text)
    exit(1)
pprint(lookup_response.json())
