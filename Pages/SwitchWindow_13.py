from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver import ActionChains
import time

class SwitchWindow():

    def __init__(self,driver):
        self.driver = driver
        self.to_switchwindow_xpath = "/html/body/div[1]/div/li[13]/a"
        self.newtabbutton_id = "new-tab-button"
        self.alertbutton_id = "alert-button"

    def clicklink(self):
        self.driver.find_element_by_xpath(self.to_switchwindow_xpath).click()

    def ClickNewTab(self):
        wait(self.driver,10).until(EC.visibility_of_element_located((By.ID,(self.newtabbutton_id))))
        self.driver.find_element_by_id(self.newtabbutton_id).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[0])

    def ClickAlert(self):
        wait(self.driver,10).until(EC.visibility_of_element_located((By.ID,(self.alertbutton_id))))
        self.driver.find_element_by_id(self.alertbutton_id).click()
        alert = self.driver.switch_to_alert()
        alert.accept()





