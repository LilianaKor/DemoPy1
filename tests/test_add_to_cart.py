import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def browser():
    """Фикстура для управления браузером"""
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


@pytest.fixture
def authorized_user(browser):
    """Фикстура для авторизованного пользователя"""
    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.NAME, "login-button").click()
    assert "inventory" in browser.current_url

    yield browser


def test_add_to_cart(authorized_user):
    authorized_user.find_element(By.XPATH, "//button[contains(text(),'Add to cart')]").click()
    authorized_user.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(4)
    assert "cart" in authorized_user.current_url
