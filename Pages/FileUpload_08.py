from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver import ActionChains

class FileUpload():

    def __init__(self, driver):
        self.driver = driver
        self.to_fileupload_xpath = "/html/body/div[1]/div/li[8]/a"
        self.upload_box_id = "file-upload-field"
        self.resetbutton_css = ".btn.btn-warning.btn-reset"

    def clicklink(self):
        self.driver.find_element_by_xpath(self.to_fileupload_xpath).click()

    def InputUpload(self, input):
        wait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, (self.upload_box_id))))
        self.driver.find_element_by_id(self.upload_box_id).send_keys(input)

    def Reset(self):
        self.driver.find_element_by_css_selector(self.resetbutton_css).click()

