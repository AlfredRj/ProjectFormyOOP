from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver import ActionChains

class Radio():

    def __init__(self,driver):
        self.driver = driver
        self.to_radio_xpath = "/html/body/div/div/li[12]/a"
        self.radiobutton1_id = "radio-button-1"
        self.radiobutton2_css = "input[value='option2']"
        self.radiobutton3_css = "input[value='option3']"

    def clicklink(self):
        self.driver.find_element_by_xpath(self.to_radio_xpath).click()

    def ClickRadio(self):
        wait(self.driver,10).until(EC.visibility_of_element_located((By.ID,(self.radiobutton1_id))))
        self.driver.find_element_by_id(self.radiobutton1_id).click()
        self.driver.find_element_by_css_selector(self.radiobutton2_css).click()
        self.driver.find_element_by_css_selector(self.radiobutton3_css).click()