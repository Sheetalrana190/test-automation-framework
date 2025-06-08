import pytest
from selenium import webdriver
import json

@pytest.fixture(scope="session")
def config():
    with open("data/config.json") as f:
        return json.load(f)

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
