from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from library import config_reader

def start_browser():
    global driver

    if((config_reader.readconfigdata('details','Browser'))=="chrome"):
        path = "./driver/chromedriver.exe"
        driver = Chrome(executable_path=path)
    elif((config_reader.readconfigdata('details','Browser'))=="firefox"):
        path = "./driver/geckodriver.exe"
        driver = Firefox(executable_path=path)
    else:
       path = "./driver/chromedriver.exe"
       driver = Chrome(executable_path=path)

    driver.get(config_reader.readconfigdata('details','Application_URL'))
    driver.maximize_window()
    return driver

def close_browser():
    driver.close()