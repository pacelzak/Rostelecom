from page_registrations import *
import os
from dotenv import load_dotenv
import pytest

load_dotenv()
email = os.getenv("email")
password = os.getenv("password")
first_name = os.getenv('first_name')
last_name = os.getenv('last_name')
incorect_password = os.getenv('incorect_password')
new_email = os.getenv('new_email')


@pytest.mark.positive_reg
def test_valid_enter(browser):

    """Успешная регистрация по email"""

    page = PageResister(browser)
    page.open_page()
    page.click_register()
    page.first_name(first_name)
    page.last_name(last_name)
    page.region(5)
    page.login(email)
    page.password(password)
    page.double_password(password)
    page.click_button_login()
    assert page.password_on_email() == True

@pytest.mark.negative_reg
def test_repeat_email(browser):

    """Регистрация с уже использованным email"""

    page = PageResister(browser)
    page.open_page()
    page.click_register()
    page.first_name(first_name)
    page.last_name(last_name)
    page.region(5)
    page.login(email)
    page.password(password)
    page.double_password(password)
    page.click_button_login()
    assert page.double_email() == True

@pytest.mark.negative_reg
def test_first_name_len_less(browser):

    """Валидация поля ИМЯ по длине минимальной"""

    page = PageResister(browser)
    page.open_page()
    page.click_register()
    page.first_name("P")
    page.last_name(last_name)
    page.region(5)
    page.login(email)
    page.password(password)
    page.double_password(password)
    page.click_button_login()
    assert page.error_message_first_name() == True

@pytest.mark.negative_reg
def test_check_password(browser):

        """Неверный в пароль в поле ПОДТВЕРЖДЕНИЯ ПАРОЛЯ"""

        page = PageResister(browser)
        page.open_page()
        page.click_register()
        page.first_name(first_name)
        page.last_name(last_name)
        page.region(5)
        page.login(email)
        page.password(password)
        page.double_password(incorect_password)
        page.click_button_login()
        assert page.error_message_check_password() == True

@pytest.mark.negative_reg
def test_len_password(browser):
    """Пароль в поле ПАРОЛЬ менее 8 символов"""

    page = PageResister(browser)
    page.open_page()
    page.click_register()
    page.first_name(first_name)
    page.last_name(last_name)
    page.region(5)
    page.login(email)
    page.password("1234!Qq")
    page.double_password("1234!Qq")
    page.click_button_login()
    assert page.error_message_password() == True

@pytest.mark.negative_reg
def test_len_max_password(browser):

    """Пароль в поле ПАРОЛЬ более 20 символов"""

    page = PageResister(browser)
    page.open_page()
    page.click_register()
    page.first_name(first_name)
    page.last_name(last_name)
    page.region(5)
    page.login(email)
    page.password("12345678910111213141516171819!Qq")
    page.double_password("12345678910111213141516171819!Qq")
    page.click_button_login()
    assert page.error_message_password() == True

@pytest.mark.negative_reg
def test_sum_password(browser):

    """Пароль в поле ПАРОЛЬ без спецсимволов"""

    page = PageResister(browser)
    page.open_page()
    page.click_register()
    page.first_name(first_name)
    page.last_name(last_name)
    page.region(5)
    page.login(email)
    page.password("1234Qq")
    page.double_password("1234Qq")
    page.click_button_login()
    assert page.error_message_password() == True


@pytest.mark.positive_reg
def test_change_email(browser):
    """Смена email при регистрации"""

    page = PageResister(browser)
    page.open_page()
    page.click_register()
    page.first_name(first_name)
    page.last_name(last_name)
    page.region(5)
    page.login(new_email)
    page.password(password)
    page.double_password(password)
    page.click_button_login()
    page.change_email_registration()
    assert "registration" in browser.current_url

@pytest.mark.negative_reg
def test_code_phone(browser):
    """Валидация номера телефона"""

    page = PageResister(browser)
    page.open_page()
    page.click_register()
    page.first_name(first_name)
    page.last_name(last_name)
    page.region(5)
    page.login("+4026954778794")
    page.password(password)
    page.double_password(password)
    page.click_button_login()
    assert page.double_email() == True

@pytest.mark.negative_reg
def test_max_len_first_name(browser):
    """Ввод максимального количества символов в поле ИМЯ"""

    page = PageResister(browser)
    page.open_page()
    page.click_register()
    page.first_name("пппрморрмиорирооциарулоиуаолуцатолаутаутагшргшргерешг")
    page.last_name(first_name)
    page.region(5)
    page.login(email)
    page.password(password)
    page.double_password(password)
    page.click_button_login()
    assert page.double_email() == True

@pytest.mark.negative_reg
def test_latin_first_name(browser):
    """Ввод латинских символов в поле ИМЯ"""

    page = PageResister(browser)
    page.open_page()
    page.click_register()
    page.first_name("Pavel")
    page.last_name(last_name)
    page.region(5)
    page.login(email)
    page.password(password)
    page.double_password(password)
    page.click_button_login()
    assert page.error_message_first_name() == True


@pytest.mark.positive_reg
def test_default_region(browser):

    "Регион по умолчанию"

    page = PageResister(browser)
    page.open_page()
    page.click_register()
    page.region(5)
    assert "Москва" in page.default_region()
