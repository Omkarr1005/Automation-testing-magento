import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def setup_new_session():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
