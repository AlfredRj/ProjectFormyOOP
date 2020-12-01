from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver import ActionChains

class Modal():

    def __init__(self,driver):
        self.driver = driver
        self.to_modal_xpath = "/html/body/div[1]/div/li[10]/a"
        self.modalbutton_id = "modal-button"
        self.closebutton_id = "close-button"

    def clicklink(self):
        self.driver.find_element_by_xpath(self.to_modal_xpath).click()

    def ClickButton(self):
        wait(self.driver, 10).until(EC.visibility_of_element_located((By.ID,(self.modalbutton_id))))
        self.driver.find_element_by_id(self.modalbutton_id).click()