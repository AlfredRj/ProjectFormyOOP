from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import time

class Complete():

    def __init__(self,driver):
        self.driver = driver
        self.to_complete_xpath = "/html/body/div[1]/div/li[14]/a"
        self.firstname_id = "first-name"
        self.lastname_id = "last-name"
        self.jobtitle_id = "job-title"
        self.radiobutton1_id = "radio-button-1"
        self.radiobutton2_id = "radio-button-2"
        self.radiobutton3_id = "radio-button-3"
        self.checkbox1_id = "checkbox-1"
        self.checkbox2_id = "checkbox-2"
        self.checkbox3_id = "checkbox-3"
        self.dropdownbox_id = "select-menu"
        self.dropdownboxoption_css = "select[value='1']"
        self.date_id = "datepicker"
        self.submitbutton_xpath = "/html/body/div[1]/form/div/div[8]/a"

    def clicklink(self):
        self.driver.find_element_by_xpath(self.to_complete_xpath).click()

    def FirstName(self,input):
        wait(self.driver,10).until(EC.visibility_of_element_located((By.ID,(self.firstname_id))))
        self.driver.find_element_by_id(self.firstname_id).send_keys(input)

    def LastName(self,input):
        self.driver.find_element_by_id(self.lastname_id).send_keys(input)

    def JobTitle(self,input):
        self.driver.find_element_by_id(self.jobtitle_id).send_keys(input)

    def RadioButton(self):
        self.driver.find_element_by_id(self.radiobutton1_id).click()
        self.driver.find_element_by_id(self.radiobutton2_id).click()
        self.driver.find_element_by_id(self.radiobutton3_id).click()

    def CheckBox(self):
        self.driver.find_element_by_id(self.checkbox1_id).click()
        self.driver.find_element_by_id(self.checkbox2_id).click()
        self.driver.find_element_by_id(self.checkbox3_id).click()

    def DropDown(self):
        # self.driver.find_element_by_id(self.dropdownbox_id).click()
        select = Select(self.driver.find_element_by_id(self.dropdownbox_id))
        select.select_by_value('1')

    def Date(self, input):
        self.driver.find_element_by_id(self.date_id).send_keys(input)

    def Submit(self):
        self.driver.find_element_by_xpath(self.submitbutton_xpath).click()



