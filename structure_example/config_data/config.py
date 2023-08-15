import os
from dotenv import load_dotenv, find_dotenv
from structure_example import database

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

DB_PATH = "structure_example/database/database.db"
BOT_TOKEN = os.getenv("BOT_TOKEN")
RAPID_API_KEY = os.getenv("RAPID_API_KEY")
YANDEX_DICT_KEY = os.getenv("YANDEX_DICT_KEY")
# DEFAULT_COMMANDS = (
#     ("start", "Запустить бота"),
#     ("help", "Вывести справку")
# )

DEFAULT_COMMANDS = (
    ('newtask', 'Создать задачу'),
    ('tasks', 'Последние 10 задач'),
    ('today', 'Задачи на сегодня')
)

DATE_FORMAT = "%d.%m.%Y"