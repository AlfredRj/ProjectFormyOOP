from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver import ActionChains

class KeyNMouse():

    def __init__(self, driver):
        self.driver = driver
        self.to_keynmouse_xpath = "/html/body/div[1]/div/li[9]/a"
        self.keynmousebox_id = "name"
        self.keynmousebutton_id = "button"

    def clicklink(self):
        self.driver.find_element_by_xpath(self.to_keynmouse_xpath).click()

    def Input(self, input):
        wait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, (self.keynmousebox_id))))
        self.driver.find_element_by_id(self.keynmousebox_id).send_keys(input)
        self.driver.find_element_by_id(self.keynmousebutton_id).click()