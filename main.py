from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
import HtmlTestRunner
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from Pages.AutoComplete_01 import AutoComplete
from Pages.Buttons_02 import Button
from Pages.Checkbox_03 import CheckBox
from Pages.DatePicker_04 import Datepicker
from Pages.DragNDrop_05 import DragNDrop
from Pages.Dropdown_06 import Dropdown
from Pages.DisabledEnabledInput_07 import Disabled
from Pages.FileUpload_08 import FileUpload
from Pages.KeyNMouse_09 import KeyNMouse
from Pages.Modal_10 import Modal
from Pages.PageScroll_11 import Scroll
from Pages.RadioButton_12 import Radio
from Pages.SwitchWindow_13 import SwitchWindow
from Pages.Complete_14 import Complete
import unittest
import time

class Formy(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    def test_01_autocomplete(self):
        driver = self.driver
        driver.get("https://formy-project.herokuapp.com/")

        autocomplete = AutoComplete(driver)
        autocomplete.clicklink()
        autocomplete.inputaddress("Jalan Wadas Raya")

    def test_02_buttons(self):
        driver = self.driver
        driver.get("https://formy-project.herokuapp.com/")

        button = Button(driver)
        button.clicklink()
        button.clickallbutton()

    def test_03_checkbox(self):
        driver = self.driver
        driver.get("https://formy-project.herokuapp.com/")

        check = CheckBox(driver)
        check.clicklink()
        check.clickallcheckboxes()

    def test_04_datepicker(self):
        driver = self.driver
        driver.get("https://formy-project.herokuapp.com/")

        date = Datepicker(driver)
        date.clicklink()
        date.DatePicker("11/30/2020")

    def test_05_dragndrop(self):
        driver = self.driver
        driver.get("https://formy-project.herokuapp.com/")

        drag = DragNDrop(driver)
        drag.clicklink()
        drag.DragNDrop()

    def test_06_dropdown(self):
        driver = self.driver
        driver.get("https://formy-project.herokuapp.com/")

        dropdown = Dropdown(driver)
        dropdown.clicklink()
        dropdown.InputDropDown()

    def test_07_disabled(self):
        driver = self.driver
        driver.get("https://formy-project.herokuapp.com/")

        disabled = Disabled(driver)
        disabled.clicklink()
        disabled.Input("Test")

    def test_08_upload(self):
        driver = self.driver
        driver.get("https://formy-project.herokuapp.com/")

        upload = FileUpload(driver)
        upload.clicklink()
        upload.InputUpload("Tugas3.docx")
        upload.Reset()

    def test_09_keynmouse(self):
        driver = self.driver
        driver.get("https://formy-project.herokuapp.com/")

        keynmouse = KeyNMouse(driver)
        keynmouse.clicklink()
        keynmouse.Input("Test")

    def test_10_modal(self):
        driver = self.driver
        driver.get("https://formy-project.herokuapp.com/")

        modal = Modal(driver)
        modal.clicklink()
        modal.ClickButton()

        time.sleep(2)
        driver.execute_script("document.getElementById('close-button').click();")

    def test_11_scroll(self):
        driver = self.driver
        driver.get("https://formy-project.herokuapp.com/")

        scroll = Scroll(driver)
        scroll.clicklink()
        time.sleep(2)
        js = "window.scrollTo(0,document.body.scrollHeight)"
        driver.execute_script(js)
        scroll.InputName("Alfred Radja Jaya")
        scroll.InputDate("11/30/2020")

    def test_12_radio(self):
        driver = self.driver
        driver.get("https://formy-project.herokuapp.com/")

        radio = Radio(driver)
        radio.clicklink()
        radio.ClickRadio()

    def test_13_switch(self):
        driver = self.driver
        driver.get("https://formy-project.herokuapp.com/")

        switch = SwitchWindow(driver)
        switch.clicklink()
        switch.ClickNewTab()
        switch.ClickAlert()

    def test_14_complete(self):
        driver = self.driver
        driver.get("https://formy-project.herokuapp.com/")

        complete = Complete(driver)
        complete.clicklink()
        complete.FirstName("Alfred")
        complete.LastName("Radja Jaya")
        complete.JobTitle("Quality Assurance")
        complete.RadioButton()
        complete.CheckBox()
        complete.DropDown()
        complete.Date("11/30/2020")
        complete.Submit()
        # page = driver.find_element_by_xpath('/html/body').text
        # self.assertTrue("Thanks for submitting your form" in page)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Success")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/alfre/PycharmProjects/ProjectFormyOOP/Report"))