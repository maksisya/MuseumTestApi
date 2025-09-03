# Тесты связанные с проверкой ответа на запрос получения объекта произведения искусства

import pytest
from main import get_museum_object, get_rand_museum_object_ids
from pydantic_models import MuseumObject


# Проверка корректности http-статуса
@pytest.mark.parametrize("id", get_rand_museum_object_ids())
def test_get_object_statuscode(id):
    response = get_museum_object(id)
    MuseumObject(**response.json())
    assert response.status_code == 200

    
# Проверка запроса с несуществующим id
def test_get_object_incorrect_id():
    response = get_museum_object(0)
    MuseumObject(**response.json())
    assert response.status_code == 404
    