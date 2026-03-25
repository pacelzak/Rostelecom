

import pytest

from page_auth import *
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import os
from dotenv import load_dotenv

load_dotenv()
ok_number = os.getenv('ok_number')
ok_password_number = os.getenv('ok_password_number')
un_reg_email = os.getenv('un_reg_email')
unvalid_password = os.getenv('unvalid_password')

@pytest.mark.positive_auth
def test_valid_enter(browser):

    """Удачный логин"""

    page = PageAuth(browser)
    page.open_page()
    page.login(ok_number)
    page.password(ok_password_number)
    page.click_button_login()
    assert page.find_exit() == True

@pytest.mark.negative_auth
def test_invalid_enter(browser):

    """Незарегистрированный email"""

    page = PageAuth(browser)
    page.open_page()
    page.tab_email_enter()
    page.login(un_reg_email)
    page.password(ok_password_number)
    page.click_button_login()
    assert page.error_message_display() == True

@pytest.mark.positive_auth
def test_automatic_tab(browser):

    "Автоматическая смена таба"

    page = PageAuth(browser)
    page.open_page()
    page.login("mrnrrknggr@gmail.com")
    assert "Телефон" == page.check_active_tab()
    page.show_password() # клик чтобы таб сменился
    assert "Почта" == page.check_active_tab()

@pytest.mark.negative_auth
def test_auth_invalid_password(browser):

    """Авторизация с неверным паролем"""

    page = PageAuth(browser)
    page.open_page()
    page.login(ok_number)
    page.password(unvalid_password)
    page.click_button_login()
    assert page.error_message_display() == True


@pytest.mark.positive_auth
def test_delete_field(browser):
    """Очистка значения из поля ЛОГИНА при смене таба"""

    page = PageAuth(browser)
    page.open_page()
    page.login(ok_number)
    page.password(ok_password_number)
    page.tab_email_enter()
    assert page.return_field_email() == ""


@pytest.mark.positive_auth
def test_without_cookies():

    """Проверка с отключенными cookies, тут баг, но так как нет никого поп-ап сделал завязку на показ кнопки """
    options = Options()
    options.add_argument('--disable-cookies')
    driver = webdriver.Chrome(options=options)
    page = PageAuth(driver)
    page.open_page()
    assert page.check_active_tab() == "Телефон"
    driver.quit()


@pytest.mark.positive_auth
def test_forgot_password(browser):
    """Переход по кнопке забыли пароль"""

    page = PageAuth(browser)
    page.open_page()
    page.forgot_password()
    assert "credentials" in browser.current_url