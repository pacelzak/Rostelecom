from locators import Auth, Login
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PageAuth:

    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 10)
        self.base_url = "https://b2c.passport.rt.ru/"
        self.driver = driver

    def open_page(self):
        self.driver.get(self.base_url)

    def login(self, login):

        find_email = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Auth.field_login))
        find_email.click()
        find_email.send_keys(login)

    def password(self, password):
        find_password =  WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Auth.field_password))
        find_password.click()
        find_password.send_keys(password)

    def show_password(self):
        click_show_password =  WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Auth.text_password))
        click_show_password.click()

    def click_button_login(self):

        enter =  WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Auth.button_enter))
        enter.click()

    def find_exit(self):
        button_exit = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Login.exit))
        return button_exit.is_displayed()

    def tab_email_enter(self):
        button_exit = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Auth.tab_email))
        button_exit.click()

    def error_message_display(self):
        error_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Auth.error_message))
        return error_message.is_displayed()

    def check_active_tab(self):

        start_tab_phone = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Auth.active_tab))
        return start_tab_phone.text

    def return_field_email(self):

        field_text = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Auth.field_login))
        return field_text.get_attribute("value")

    def forgot_password(self):

        button_forgot_password = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Auth.forgot_password))
        button_forgot_password.click()









