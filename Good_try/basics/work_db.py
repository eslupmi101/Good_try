import os
import json

from .models import Data


def update_accomodation():
    if is_new_accommodation():
        add_new_accommodation()
        clean_json()


def is_new_accommodation() -> bool:
    """
    Функция для проверки, является ли файл new_accomodation.json пустым в предыдущей папке.
    :return: True, если файл пустой, и False, если файл содержит данные.
    """
    # Получаем путь к текущей директории и предыдущей директории
    current_dir = os.path.abspath(os.path.dirname(__file__))
    parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

    # Получаем путь к файлу new_accomodation.json в предыдущей директории
    new_accomodationjson_path = os.path.join(parent_dir, "new_accomodation.json")

    # Проверяем, пустой ли файл
    with open(new_accomodationjson_path, "r") as f:
        data = json.load(f)
        if data:
            return True
        else:
            return False


def add_new_accommodation():
    current_dir = os.path.abspath(os.path.dirname(__file__))
    parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

    # Получаем путь к файлу new_accomodation.json в предыдущей директории
    new_accomodationjson_path = os.path.join(parent_dir,
                                             "new_accomodation.json")

    # Считываем содержимое файла в словарь
    with open(new_accomodationjson_path, "r") as f:
        new_accomodations = json.load(f)
    for details in new_accomodations['Accoms']:
        data = Data()
        data.title = details['title']
        data.accommodation_type = details['accommodation_type']
        data.description = details['description']
        data.address = details['address']
        data.img_url = details['img_url']
        data.price = details['price']
        data.contact_phone = details['contact_phone']
        data.contact_email = details['contact_email']
        data.save()


def clean_json():
    current_dir = os.path.abspath(os.path.dirname(__file__))
    parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

    # Получаем путь к файлу new_accomodation.json в предыдущей директории
    new_accomodationjson_path = os.path.join(parent_dir,
                                             "new_accomodation.json")

    # Очищаем содержимое файла
    with open(new_accomodationjson_path, "w") as f:
        json.dump({}, f)
