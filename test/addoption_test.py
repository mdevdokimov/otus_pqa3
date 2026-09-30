import pytest
import requests

TIMEOUT=3


def test_get_public_users(base_url, status_code):
    # print(base_url)
    response = requests.get(base_url, timeout=TIMEOUT)
    assert response.status_code == int(status_code)