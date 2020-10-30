from base_files import initiate_driver
from library import config_reader
from pages import reg_page

def test_reg_invalid():
    driver = initiate_driver.start_browser()
    reg = reg_page.regclass(driver)
    reg.enter_country()
    driver.close()