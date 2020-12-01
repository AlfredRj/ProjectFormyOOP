from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver import ActionChains

class Scroll():

    def __init__(self,driver):
        self.driver = driver
        self.to_pagescroll_xpath = "/html/body/div[1]/div/li[11]/a"
        self.name_box_id = "name"
        self.date_box_id = "date"

    def clicklink(self):
        self.driver.find_element_by_xpath(self.to_pagescroll_xpath).click()

    def InputName(self, input):
        wait(self.driver,10).until(EC.visibility_of_element_located((By.ID,(self.name_box_id))))
        self.driver.find_element_by_id(self.name_box_id).send_keys(input)


    def InputDate(self,date):
        self.driver.find_element_by_id(self.date_box_id).send_keys(date)