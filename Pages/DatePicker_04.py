from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait

class Datepicker():

    def __init__(self, driver):
        self.driver = driver
        self.to_datepicker_xpath = "/html/body/div[1]/div/li[4]/a"
        self.date_box_id = "datepicker"

    def clicklink(self):
        self.driver.find_element_by_xpath(self.to_datepicker_xpath).click()

    def DatePicker(self, tanggal):
        wait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, (self.date_box_id))))
        self.driver.find_element_by_id(self.date_box_id).send_keys(tanggal)