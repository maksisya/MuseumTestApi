# Тесты связанные с проверкой ответа на запрос получения объекта произведения искусства

from main import get_museum_object
from pydantic_models import MuseumObject


# Проверка запроса получения объекта произведения искусства по id
def test_getobject_statuscode():
    response = get_museum_object(436803)
    museum_object = MuseumObject(**response.json())
    assert response.status_code == 200
    assert museum_object.objectID == 436803
    assert museum_object.isHighlight == False
    assert museum_object.accessionYear == '1941'
    
# Проверка запроса с несуществующим id
def test_getobject_incorrectid():
    response = get_museum_object(0)
    MuseumObject(**response.json())
    assert response.status_code == 404
    