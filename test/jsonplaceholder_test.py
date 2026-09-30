import pytest
import requests

TIMEOUT=3


def test_get():
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1', timeout=TIMEOUT)
    resp = response.json()
    assert response.status_code == 200
    assert resp["userId"]
    assert resp["id"]
    assert resp["title"]
    assert resp["body"]


def test_list():
    response = requests.get('https://jsonplaceholder.typicode.com/posts', timeout=TIMEOUT)
    resp = response.json()
    assert response.status_code == 200
    assert len(resp) > 1


create_data = [
    {"userId":1, "title":"test1111", "body":"1!!111!!!"},
    {"userId":2, "title":"test2222", "body":"2@@@@@@2222@2"}
]
@pytest.mark.parametrize("data", create_data)
def test_create(data):
    response = requests.post('https://jsonplaceholder.typicode.com/posts', json=data, timeout=TIMEOUT)
    resp = response.json()
    assert response.status_code == 201
    assert resp["id"] == 101


def test_update():
    data = {"id":1, "userId":1, "title":"test1111", "body":"1!!111!!!"}
    response = requests.put('https://jsonplaceholder.typicode.com/posts/1', json=data, timeout=TIMEOUT)
    resp = response.json()
    assert response.status_code == 200
    assert resp["id"] == 1
    assert resp["userId"] == 1
    assert resp["title"] == "test1111"
    assert resp["body"] == "1!!111!!!"


patch_data = [
    {"body":"LEEEEEROOOOY!!!1!11!!"},
    {"title":"NEW TITLE"}
]
@pytest.mark.parametrize("data", patch_data)
def test_patch(data):
    response = requests.patch('https://jsonplaceholder.typicode.com/posts/1', json=data, timeout=TIMEOUT)
    resp = response.json()
    print(resp)
    assert response.status_code == 200
