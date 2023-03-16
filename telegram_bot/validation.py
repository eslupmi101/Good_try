import json

key = '456'
desc = 'Lord'

val_file = 'key_list.json'
user_f = 'users.json'
agent_f = 'for_agents.json'
pend_f = 'pending.json'
site_f = 'for_site.json'
shit = 'I shat myself'


def user_vald(user_id):
    ans = [False, '']
    try:
        with open(user_f, 'r') as f:
            data = json.load(f)
            f.close()
        for u in data['users']:
            if u['user_id'] == str(user_id):
                ans = [True, u['user_type']]
    except:
        ans = [False, 'I shat myself']
    finally:
        return ans


def add_user(user_id, user_type, key):
    new_user = {
        'user_id': str(user_id),
        'user_type': user_type,
        'key': str(key)
    }
    if user_vald(user_id)[0]:
        return
    try:
        with open(user_f, 'r') as f:
            data = json.load(f)
            f.close()
        data['users'].append(new_user)
        with open(user_f, 'w') as f:
            json.dump(data, f)
            f.close()
    finally:
        return


def key_vald(key):
    ans = [False, '']
    try:
        with open(val_file, 'r') as f:
            data = json.load(f)
            for k in data['keys']:
                if str(k['key']) == str(key):
                    f.close()
                    ans = [True, k['description']]
    finally:
        return ans


def add_key(key, description):
    new_key = {
        'key': str(key),
        'description': description
    }
    val = key_vald(key)
    if val[0]:
        return
    try:
        with open(val_file, 'r') as f:
            data = json.load(f)
            f.close()
    except:
        data = {
            'keys': []
        }
    with open(val_file, 'w') as f:
        data['keys'].append(new_key)
        json.dump(data, f)
        f.close()


def are_they(user_id, user_type):
    ans, u_type = user_vald(user_id)
    if ans and u_type == user_type:
        return True
    return False


def get_user_key(user_id):
    res = [False, shit]
    try:
        with open(user_f, 'r') as f:
            data = json.load(f)
            for u in data['users']:
                if u['user_id'] == user_id:
                    res = [True, u['key']]
            f.close()
    finally:
        return res

def get_agent_id_from_lord_key(key):
    res = [False, shit]
    try:
        with open(user_f, 'r') as f:
            data = json.load(f)
            for u in data['users']:
                try:
                    if u['lord_key'] == str(key):
                        res = [True, u['user_id']]
                except:
                    pass
            f.close()
    finally:
        return res


def add_appl(text, lord_id):
    suc, lord_key = get_user_key(lord_id)
    if not suc:
        return False
    suc, agent_id = get_agent_id_from_lord_key(lord_key)
    if not suc:
        return False
    new_appl = {
        'text': text,
        'lord_id': lord_id,
        'agent_id': agent_id
    }
    try:
        with open(agent_f, 'r') as f:
            data = json.load(f)
            f.close()
        data['applications'].append(new_appl)
        with open(agent_f, 'w') as f:
            json.dump(data, f)
            f.close()
        return True
    except:
        return False

def get_appl_by_id(agent_id):
    res = [False, '']
    try:
        with open(agent_f) as f:
            data = json.load(f)
            f.close()
        for a in data['applications']:
            if a['agent_id'] == str(agent_id):
                res = [True, a]
                data['applications'].remove(a)
                with open(agent_f, 'w') as f:
                    json.dump(data, f)
                    f.close()
    finally:
        return res

def add_to_pend(agent_id, appl):
    res = False
    try:
        with open(pend_f, 'r') as f:
            data = json.load(f)
            f.close()
        new_appl = {
            'agent_id': agent_id,
            'appl': appl
        }
        data['pending'].append(new_appl)
        with open(pend_f, 'w') as f:
            json.dump(data, f)
            f.close()
        res = True
    finally:
        return res


def get_pending_by_id(agent_id):
    res = [False, '']
    try:
        with open(pend_f, 'r') as f:
            print('open ok')
            data = json.load(f)
            f.close()
        print(data)
        for a in data['pending']:
            if str(a['agent_id']) == str(agent_id):
                appl = a['appl']
                res = [True, appl]
                data['pending'].remove(a)
                with open(pend_f, 'w') as f:
                    json.dump(data, f)
                    f.close()
    finally:
        return res


def add_for_site(appl):
    res = False
    try:
        with open(site_f, 'r') as f:
            data = json.load(f)
            f.close()
        appl_new = {
            "title": appl['text'],
            "accommodation_type": "lorem",
            "description": appl['text'],
            "address": "lorem",
            "img_url": "img",
            "price": "9999",
            "contact_phone": appl['lord_id'],
            "contact_email": "mail"
        }
        data['Accoms'].append(appl_new)
        with open(site_f, 'w') as f:
            json.dump(data, f)
            f.close()
        res = True
    finally:
        return res


if __name__ == '__main__':
    add_key(key, desc)
    user_id = "234"
    user_type = "User"
    user_key = '123'
    add_user(user_id, user_type, user_key)
    print(user_vald(user_id))