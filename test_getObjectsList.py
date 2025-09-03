# Тесты связанные с проверкой ответа на запрос получения списка произведений искусства

from main import get_museum_objects_list
from pydantic_models import ObjectsList


# Проверка получения списка произведения искусства по ключевому слову
def test_get_objectlist():
    payload = {
        "q": "sunflowers",
        "isHighlight": "true"
    }
    response = get_museum_objects_list(payload)
    objects_list = ObjectsList(**response.json())
    assert response.status_code == 200
    assert objects_list.total == 3
    assert objects_list.objectIDs == [206989, 437261, 626692]


# Список произведений в период времени + по ключевому слову
def test_get_objects_list_of_daterange():
    payload = {
        "dateBegin": "1700",
        "dateEnd": "1800",
        "q": "African"
    }
    response = get_museum_objects_list(payload)
    objects_list = ObjectsList(**response.json())
    assert response.status_code == 200
    assert objects_list.total == 108


# Получаем больше произведений, чем указано ограничение в модели 
def test_get_object_list_more_then_max():
    payload = {
        "q": "African"
    }
    response = get_museum_objects_list(payload)
    objects_list = ObjectsList(**response.json())
    assert response.status_code == 200
    assert objects_list.total == 3484
