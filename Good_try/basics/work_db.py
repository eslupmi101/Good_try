import json
from .models import Data


n_acc_dir = '/Users/ajsenandreev/home/pet_projects/MPIT/test1/Good_try/Good_try/new_accomodation.json'


def update_accomodation():
    if is_new_accommodation():
        add_new_accommodation()
        clean_json()


def get_data():
    res = None
    try:
        with open(n_acc_dir) as f:
            data = json.load(f)
            f.close()
        res = data
    finally:
        return res


def is_new_accommodation() -> bool:
    # if true then there are accomodations to add to website
    data = get_data()
    if data is None:
        Exception('cant read new accomodation json')
    else:
        acc_list = data['Accoms']
        if len(acc_list) > 0:
            return True
        return False


def add_new_accommodation():
    new_accomodations = get_data()
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
    data = get_data()
    res = False
    if data is None:
        return False
    try:
        data['Accoms'].clear()
        with open(n_acc_dir, 'w') as f:
            json.dump(data, f)
            f.close()
        res = True
    finally:
        return res
