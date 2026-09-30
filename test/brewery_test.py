import pytest
import requests

TIMEOUT=3

def test_single():
    obdb_id = "b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0"
    response = requests.get(f'https://api.openbrewerydb.org/v1/breweries/{obdb_id}', timeout=TIMEOUT)
    resp = response.json()
    assert response.status_code == 200
    assert resp["id"] == obdb_id


def test_list():
    pages = 10
    response = requests.get(f'https://api.openbrewerydb.org/v1/breweries?per_page={pages}', timeout=TIMEOUT)
    resp = response.json()
    assert response.status_code == 200
    assert len(resp) == pages


def test_random():
    size = {'size': 3}
    response = requests.get('https://api.openbrewerydb.org/v1/breweries/random', params=size, timeout=TIMEOUT)
    resp = response.json()
    assert response.status_code == 200
    assert len(resp) == size['size']


search_data = [
    {"query":"San Diego", "per_page":30, "search_in_resp": {"city":"San Diego"}},
    {"query":"planning", "per_page":10, "search_in_resp": {"brewery_type":"planning"}},
    {"query":"6198233402", "per_page":5, "search_in_resp": {"phone":"6198233402"}}
]
@pytest.mark.parametrize("data", search_data)
def test_search(data):
    response = requests.get(f'https://api.openbrewerydb.org/v1/breweries/search?query={data["query"]}&per_page={data["per_page"]}', timeout=TIMEOUT)
    # print(response.url)
    resp = response.json()
    key, value = list(data["search_in_resp"].items())[0] # ключ и занчение из search_in_resp из data
    assert response.status_code == 200
    # тут убедимся, что поиск был успешен и мы действительно нашли в ответах то, что искали
    # ну и ищем только в первом словаре, т.к. не понятно сколько оно вернёт в ответе
    # верю, что ответ будет не нулевым
    assert resp[0].get(key) == value

meta_data = [
    {"by_country":"Australia"},
    {"by_type":"micro"}
]
@pytest.mark.parametrize("data", meta_data)
def test_metadata(data):
    response = requests.get('https://api.openbrewerydb.org/v1/breweries/meta', params=data, timeout=TIMEOUT)
    resp = response.json()
    assert response.status_code == 200
    assert resp["total"] != 0
