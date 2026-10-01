import pytest
import requests


def test_get_public_users(base_url, status_code, timeout):
    # print(base_url)
    response = requests.get(base_url, timeout=timeout)
    assert response.status_code == int(status_code)