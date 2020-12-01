from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait


class AutoComplete():

    def __init__(self, driver):
        self.driver = driver
        self.to_autocomplete_css = ".btn.btn-lg"
        self.address_id = "autocomplete"

    def clicklink(self):
        self.driver.find_element_by_css_selector(self.to_autocomplete_css).click()

    def inputaddress(self, address):
        wait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, (self.address_id))))
        self.driver.find_element_by_id(self.address_id).clear()
        self.driver.find_element_by_id(self.address_id).send_keys(address)