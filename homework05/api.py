from typing import Optional

import requests
import time
import config


def get(url: str, params={}, timeout=5, max_retries=5,
        backoff_factor=0.3) -> Optional[requests.models.Response]:
    """ Выполнить GET-запрос
    :param url: адрес, на который необходимо выполнить запрос
    :param params: параметры запроса
    :param timeout: максимальное время ожидания ответа от сервера
    :param max_retries: максимальное число повторных запросов
    :param backoff_factor: коэффициент экспоненциального нарастания задержки
    """
    for i in range(max_retries):
        try:
            response = requests.get(url, params=params, timeout=timeout)
            return response
        except requests.exceptions.RequestException:
            if i == max_retries - 1:
                raise
            delay = backoff_factor * 2 ** i
            time.sleep(delay)


def get_friends(user_id: int, fields: str):
    """ Вернуть данных о друзьях пользователя
    :param user_id: идентификатор пользователя, список друзей которого нужно получить
    :param fields: список полей, которые нужно получить для каждого пользователя
    """

    assert isinstance(user_id, int), "user_id must be positive integer"
    assert isinstance(fields, str), "fields must be string"
    assert user_id > 0, "user_id must be positive integer"

    domain = "https://api.vk.com/method"
    access_token = "31df23e781b9dcfa6d421530da14b9de331c3707f34d245cede1e3e4c7eb04639e398c20454544edb98b4"
    v = '5.103'
    query = f"{domain}/friends.get?access_token={access_token}&user_id={user_id}&fields={fields}&v={v}"
    response = get(query)
    friends = response.json()
    return friends

def get_id(user_id, fields):
    """ Returns a list of user IDs or detailed information about a user's friends """
    assert isinstance(user_id, int), "user_id must be positive integer"
    assert isinstance(fields, str), "fields must be string"
    assert user_id > 0, "user_id must be positive integer"
    domain = "https://api.vk.com/method"
    access_token = "1730f20585109459c35f41d8917078ebcaf456b666599448eea70cad3c30e3d246a48a8d0610f53c341a8"
    v = '5.103'
    query = f"{domain}/friends.get?access_token={access_token}&user_id={user_id}&fields={fields}&v={v}"
    response = requests.get(query)
    x =  response.json()['response']['items']
    ids = []
    for lists in x:
        if not 'id' in lists:
            continue
        else:
            ids.append(lists['id'])
    return ids




def get_names(user_id: int, fields: str):
    """ Вернуть данных о друзьях пользователя
    :param user_id: идентификатор пользователя, список друзей которого нужно получить
    :param fields: список полей, которые нужно получить для каждого пользователя
    """

    assert isinstance(user_id, int), "user_id must be positive integer"
    assert isinstance(fields, str), "fields must be string"
    assert user_id > 0, "user_id must be positive integer"

    domain = "https://api.vk.com/method"
    access_token = "1730f20585109459c35f41d8917078ebcaf456b666599448eea70cad3c30e3d246a48a8d0610f53c341a8"
    v = '5.103'
    query = f"{domain}/friends.get?access_token={access_token}&user_id={user_id}&fields={fields}&v={v}"
    response = get(query)
    response = requests.get(query)
    x = response.json()['response']['items']
    names =[]
    for lists in x:
        if not 'first_name' and 'last_name' in lists:
            continue
        else:
            names.append(lists['first_name'] + " " + lists['last_name'])
    return names


