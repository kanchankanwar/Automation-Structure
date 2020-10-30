from selenium.webdriver import Chrome
from base_files import initiate_driver
from library import config_reader
from pages import reg_page
import pytest
import openpyxl
from dataGenerator import datagen


@pytest.mark.parametrize('data',datagen.datagenerator())
def test_Viladate_reg(data):
    driver = initiate_driver.start_browser()
    reg = reg_page.regclass(driver)
    reg.enter_username(data[0])
    reg.enter_email(data[1])
    reg.enter_password(data[2])
    driver.close()


