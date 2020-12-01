from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait


class Button():

    def __init__(self, driver):
        self.driver = driver
        self.to_button_xpath = "/html/body/div[1]/div/li[2]/a"
        self.buttonprimary_xpath = "/html/body/div[1]/form/div[1]/div/div/button[1]"
        self.buttonsuccess_xpath = "/html/body/div[1]/form/div[1]/div/div/button[2]"
        self.buttoninfo_xpath = "/html/body/div[1]/form/div[1]/div/div/button[3]"
        self.buttonwarning_xpath = "/html/body/div[1]/form/div[1]/div/div/button[4]"
        self.buttondanger_xpath = "/html/body/div[1]/form/div[1]/div/div/button[5]"
        self.buttonlink_xpath = "/html/body/div[1]/form/div[1]/div/div/button[6]"
        self.buttonleft_xpath = "/html/body/div[1]/form/div[2]/div/div/div/button[1]"
        self.buttonmid_xpath = "/html/body/div[1]/form/div[2]/div/div/div/button[2]"
        self.buttonright_xpath = "/html/body/div[1]/form/div[2]/div/div/div/button[3]"
        self.button1_xpath = "/html/body/div[1]/form/div[3]/div/div/div/button[1]"
        self.button2_xpath = "/html/body/div[1]/form/div[3]/div/div/div/button[2]"
        self.buttondropdown_id = "btnGroupDrop1"
        self.buttondropdown1_xpath = "/html/body/div[1]/form/div[3]/div/div/div/div/div/a[1]"
        self.buttondropdown2_xpath = "/html/body/div[1]/form/div[3]/div/div/div/div/div/a[2]"

    def clicklink(self):
        self.driver.find_element_by_xpath(self.to_button_xpath).click()


    def clickallbutton(self):
        wait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, (self.buttonprimary_xpath))))
        self.driver.find_element_by_xpath(self.buttonprimary_xpath).click()
        self.driver.find_element_by_xpath(self.buttonsuccess_xpath).click()
        self.driver.find_element_by_xpath(self.buttoninfo_xpath).click()
        self.driver.find_element_by_xpath(self.buttonwarning_xpath).click()
        self.driver.find_element_by_xpath(self.buttondanger_xpath).click()
        self.driver.find_element_by_xpath(self.buttonlink_xpath).click()
        self.driver.find_element_by_xpath(self.buttonleft_xpath).click()
        self.driver.find_element_by_xpath(self.buttonmid_xpath).click()
        self.driver.find_element_by_xpath(self.buttonright_xpath).click()
        self.driver.find_element_by_xpath(self.button1_xpath).click()
        self.driver.find_element_by_xpath(self.button2_xpath).click()
        self.driver.find_element_by_id(self.buttondropdown_id).click()
        self.driver.find_element_by_xpath(self.buttondropdown1_xpath).click()
        self.driver.find_element_by_id(self.buttondropdown_id).click()
        self.driver.find_element_by_xpath(self.buttondropdown2_xpath).click()


