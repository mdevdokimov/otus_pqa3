import pytest


@pytest.fixture
def status_code(request):
    return request.config.getoption("--timeout")

@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")

@pytest.fixture
def status_code(request):
    return request.config.getoption("--status_code")


def pytest_addoption(parser):
    parser.addoption(
        "--timeout", 
        action="store", 
        default=3, 
        help="таймаут ответа от сервера"
    )
    parser.addoption(
        "--url", 
        action="store", 
        default="http://ya.ru", 
        help="URL для запроса. дефолт ya.ru"
    )
    parser.addoption(
            "--status_code", 
            action="store", 
            default=200, 
            help="Статус код. дефолт 200"
    )