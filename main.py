import requests
from random import randint


# Запрос на получение объекта произведения искусства 436803
def get_museum_object(obj_id):
    r = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{obj_id}")
    return r


# Запрос на получение списка объектов произведений искусства
def get_museum_objects_list(payload):
    r = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/search", params=payload)
    return r


# Генерация списка из трёх случайных id объектов произведений искусства
def get_rand_museum_object_ids():
    rand_obj_id_arr = []
    for i in range(3):
        rand_obj_id_arr.append(randint(10000, 500000))
    return rand_obj_id_arr
