import pytest
import requests


def test_get_all(timeout):
    response = requests.get('https://dog.ceo/api/breeds/list/all', timeout=timeout)
    resp = response.json()
    assert response.status_code == 200
    assert resp["status"] == "success"


def test_random(timeout):
    response = requests.get('https://dog.ceo/api/breeds/image/random', timeout=timeout)
    resp = response.json()
    assert response.status_code == 200
    assert resp["status"] == "success"
    if "jpg" in resp["message"]:
        assert True
    else:
        assert False, "Кажется, в ответе нет картинки"


multiple_params = [
    (1,1),
    (10,10),
    (50,50),
    (100,50) # больше 50 картинок не отдает
]
@pytest.mark.parametrize("num, resp_len", multiple_params)
def test_multiple_random(num, resp_len, timeout):
    response = requests.get(f'https://dog.ceo/api/breeds/image/random/{num}', timeout=timeout)
    resp = response.json()
    assert response.status_code == 200
    assert resp["status"] == "success"
    assert len(resp["message"]) == resp_len


breeds = [
    "akita",
    "bullterrier",
    "malamute",
    "spaniel"
]
@pytest.mark.parametrize("breed", breeds)
def test_images_by_breed(breed, timeout):
    response = requests.get(f'https://dog.ceo/api/breed/{breed}/images', timeout=timeout)
    resp = response.json()
    assert response.status_code == 200
    assert resp["status"] == "success"
    assert 'message' in response.text


sub_breeds = [
    "terrier/border",
    "spitz/japanese",
    "australian/shepherd"
]
@pytest.mark.parametrize("sub_breed", sub_breeds)
def test_images_by_sub_breeds(sub_breed, timeout):
    response = requests.get(f'https://dog.ceo/api/breed/{sub_breed}/images', timeout=timeout)
    resp = response.json()
    assert response.status_code == 200
    assert resp["status"] == "success"
    assert 'message' in response.text
