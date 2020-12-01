from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver import ActionChains

class Dropdown():

    def __init__(self,driver):
        self.driver = driver
        self.to_dropdown_xpath = "/html/body/div[1]/div/li[6]/a"
        self.dropdown_box_id = "dropdownMenuButton"
        self.dropdown_menu_dropdown_xpath = "/html/body/div[1]/div/div/a[6]"

    def clicklink(self):
        self.driver.find_element_by_xpath(self.to_dropdown_xpath).click()

    def InputDropDown(self):
        wait(self.driver,10).until(EC.visibility_of_element_located((By.ID, (self.dropdown_box_id))))
        self.driver.find_element_by_id(self.dropdown_box_id).click()
        self.driver.find_element_by_xpath(self.dropdown_menu_dropdown_xpath).click()
