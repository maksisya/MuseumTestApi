import requests
from pydantic_models import ObjectsList


# Запрос на получение объекта произведения искусства 436803
def get_museum_object(obj_id):
    r = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{obj_id}")
    # MuseumObject(**r.json())
    return r


# Запрос на получение списка объектов произведений искусства
def get_museum_objects_list(payload):
    r = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/search", params=payload)
    # ObjectsList(**r.json())
    return r
