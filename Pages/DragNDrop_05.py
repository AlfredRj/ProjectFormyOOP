from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver import ActionChains

class DragNDrop():

    def __init__(self,driver):
        self.driver = driver
        self.to_dragndrop_xpath = "/html/body/div[1]/div/li[5]/a"
        self.imagepath_xpath = "/html/body/div[1]/div[1]/img"
        self.boxpath_id = "box"

    def clicklink(self):
        self.driver.find_element_by_xpath(self.to_dragndrop_xpath).click()

    def DragNDrop(self):
        action = ActionChains(self.driver)
        wait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, (self.imagepath_xpath))))
        action.drag_and_drop(self.driver.find_element_by_xpath(self.imagepath_xpath),self.driver.find_element_by_id(self.boxpath_id))



