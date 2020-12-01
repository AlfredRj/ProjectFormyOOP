from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait


class CheckBox():

    def __init__(self, driver):
        self.driver = driver
        self.to_checkbox_xpath = "/html/body/div[1]/div/li[3]/a"
        self.checkbox1_css = "input[value='checkbox-1']"
        self.checkbox2_css = "input[value='checkbox-2']"
        self.checkbox3_css = "input[value='checkbox-3']"

    def clicklink(self):
        self.driver.find_element_by_xpath(self.to_checkbox_xpath).click()

    def clickallcheckboxes(self):
        wait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, (self.checkbox1_css))))
        self.driver.find_element_by_css_selector("input[value='checkbox-1']").click()
        self.driver.find_element_by_css_selector("input[value='checkbox-2']").click()
        self.driver.find_element_by_css_selector("input[value='checkbox-3']").click()
