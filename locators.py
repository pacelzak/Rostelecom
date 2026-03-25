from selenium.webdriver.common.by import By

class Auth:

    tab_phone = (By.XPATH, '//*[@id="t-btn-tab-phone"]')
    tab_email = (By.XPATH, '//*[@id="t-btn-tab-mail"]')
    active_tab = (By.CSS_SELECTOR, ".rt-tab--active")
    tab_login = (By.XPATH, '//*[@id="t-btn-tab-login"]')
    tab_ls = (By.XPATH, '//*[@id="t-btn-tab-ls"]')
    field_login = (By.XPATH, '//*[@id="username"]')
    field_password = (By.XPATH, '//*[@id="password"]')
    text_password = (By.XPATH, "//div[contains(@class, 'rt-input__action')]")
    button_enter = (By.XPATH, '//*[@id="kc-login"]')
    button_registration = (By.XPATH, '//*[@id="kc-register"]')
    link_personal_data = (By.XPATH, '//*[@id="rt-auth-pdn-link"]')
    link_user_accept = (By.XPATH, '//*[@id="rt-auth-agreement-link"]')
    error_message = (By.XPATH, '//*[@id="page-right"]/div/div[1]/div[1]')
    forgot_password = (By.XPATH, '//*[@id="forgot_password"]')

class Registration:

    first_name = (By.XPATH, '//input[@name="firstName"]')
    last_name = (By.XPATH, '//input[@name="lastName"]')
    region = (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[2]/div/div/input')
    drop_down_region = (By.CSS_SELECTOR, '.rt-select__list-item')
    email = (By.XPATH, '//*[@id="address"]')
    password = (By.XPATH, '//*[@id="password"]')
    double_password = (By.XPATH, '//*[@id="password-confirm"]')
    click_enter = (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/button[1]')
    check_email = (By.XPATH, '//*[@id="page-right"]/div')
    modal_double_email = (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div/div')
    first_name_error = (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/span')
    error_check_password = (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[4]/div[2]/span')
    error_password = (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[4]/div[1]/span')
    change_email = (By.XPATH, '//*[@id="otp-back"]')

class ConfirmRegistration:

    change_email = (By.XPATH, '//*[@id="otp-back"]')

class Login:

    exit = (By.XPATH, '//*[@id="logout-btn"]')



