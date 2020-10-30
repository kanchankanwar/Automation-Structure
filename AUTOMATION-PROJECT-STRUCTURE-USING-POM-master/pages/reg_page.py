from library import config_reader
#from selenium.webdriver import Chrome


class regclass:

    def __init__(self, obj):
        global driver
        driver = obj

    def enter_username(self, username):
        driver.find_element_by_name(config_reader.fetch_element("registration", "user_name")).send_keys(username)

    def enter_email(self, email):
        driver.find_element_by_name(config_reader.fetch_element("registration", "email")).send_keys(email)

    def enter_password(self, password):
        driver.find_element_by_name(config_reader.fetch_element("registration", "password")).send_keys(password)

    def enter_country(self):
        driver.find_element_by_name(config_reader.fetch_element("registration", "country")).click()
