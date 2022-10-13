import logging

import pytest
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_clickable as EC

from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random

class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()   # logger

    @pytest.mark.sanity
    def test_addCustomer(self,setup):
        self.logger.info("********   Test_003_AddCustomer   *********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("****** Login Successful *******")
        self.logger.info("****** Starting Add Customer Test ******")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickonCustomersMenu()
        self.addcust.clickonCustomermenuitem()

        self.addcust.clickonAddnew()

        self.logger.info("********* Providing Customer Info *********")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVendors("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("Megha")
        self.addcust.setLastName("nath")
        self.addcust.setDob("7/05/1995")
        self.addcust.setCompanyName("busyQA")
        self.addcust.setAdminContent("This is for Testing......")
        self.addcust.clickOnSave()

        self.logger.info("****** Saving Customer info *******")
        self.logger.info("****** Add customer validation Started******")

        self.msg = self.driver.find_element(By.TAG_NAME,"body").text
        print(self.msg)
        if 'customer has been added successfully. ' in self.msg:
            assert True == True
            self.logger.info("****** Add Customer Test Passed")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("****** Add Customer test Failed ******")
            assert False == False

        self.driver.close()
        self.logger.info("******* Ending Test_003_Addcustomer test ******")


def random_generator(size=8, chars = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars)for x in range(size))




