import configuration1

import requests


import data


def get_docs():
    return requests.get(configuration1.URL_SERVICE + configuration1.DOC_PATH)

    response = get_docs()
    print(response.status_code)


def get_logs():
    return requests.get(configuration1.URL_SERVICE + configuration1.LOG_MAIN_PATH)


    response = get_logs()
    print(response.status_code)
    print(response.headers)


def get_logs():
    return requests.get(configuration1.URL_SERVICE + configuration1.LOG_MAIN_PATH,
     params={"count": 20})


def get_users_table():
    return requests.get(configuration1.URL_SERVICE + configuration1.USERS_TABLE_PATH)

    response = get_users_table()
    print(response.status_code)

    response = get_logs()
    print(response.status_code)
    print(response.headers)
    response = get_users_table()


def post_new_user(body):
    return requests.post(configuration1.URL_SERVICE + configuration1.CREATE_USER_PATH, json=body, headers=data.headers)

    response = post_new_user(data.user_body);

    print(response.status_code)
    print(response.headers)
    print(response.json())

def post_products_kits(products_ids):
    return requests.post(configuration1.URL_SERVICE + configuration1.PRODUCTS_KITS_PATH, json=products_ids,
    headers=data.headers)

    response = post_products_kits(data.product_ids);
    print(response.status_code)
    print(response.json())
