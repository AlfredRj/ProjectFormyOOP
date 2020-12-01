from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver import ActionChains

class Disabled():

    def __init__(self,driver):
        self.driver = driver
        self.to_disabled_xpath = "/html/body/div[1]/div/li[7]/a"
        self.input_box_id = "input"

    def clicklink(self):
        self.driver.find_element_by_xpath(self.to_disabled_xpath).click()

    def Input(self, input):
        wait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, (self.input_box_id))))
        self.driver.find_element_by_id(self.input_box_id).send_keys(input)



