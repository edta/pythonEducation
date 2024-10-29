import pytest
import requests
from selenium import webdriver


@pytest.fixture()
def get_joke():
    response = requests.get("https://geek-jokes.sameerkumar.website/api")
    yield response.text


@pytest.fixture(autouse=True)
def driver(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    yield driver
    driver.close()
