
from locators import Auth, Registration
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageResister:

    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 10)
        self.base_url = "https://b2c.passport.rt.ru/"
        self.driver = driver

    def open_page(self):
        self.driver.get(self.base_url)

    def click_register(self):

        button_register = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Auth.button_registration))
        button_register.click()

    def first_name(self, name):

        field_first_name = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Registration.first_name))
        field_first_name.click()
        field_first_name.send_keys(name)

    def last_name(self, name):

        field_last_name = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Registration.last_name))
        field_last_name.click()
        field_last_name.send_keys(name)

    def region(self, index):

        regions_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Registration.region))
        regions_field.click()
        options = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(Registration.drop_down_region))
        options[index].click()

    def login(self, text_login):

        field_login = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Registration.email))
        field_login.click()
        field_login.send_keys(text_login)

    def password(self, text_password):
        field_password = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Registration.password))
        field_password.click()
        field_password.send_keys(text_password)

    def double_password(self, text_double_password):
        field_double_password = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Registration.double_password))
        field_double_password.click()
        field_double_password.send_keys(text_double_password)

    def click_button_login(self):

        button_enter = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Registration.click_enter))
        button_enter.click()

    def password_on_email(self):
        field_password = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Registration.check_email))
        return field_password.is_displayed()

    def double_email(self):
        modal_email = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Registration.modal_double_email))
        return modal_email.is_displayed()

    def error_message_first_name(self):
        error_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Registration.first_name_error))
        return error_message.is_displayed()

    def error_message_check_password(self):
        error_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Registration.error_check_password))
        return error_message.is_displayed()

    def error_message_password(self):
        error_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Registration.error_password))
        return error_message.is_displayed()

    def change_email_registration(self):

        button_change_email = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Registration.change_email))
        button_change_email.click()

    def default_region(self):
        region = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Registration.region))
        return region.get_attribute("value")

