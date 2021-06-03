import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random
class Test_003_AddCustomer:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_addCustomer(self,setup):
        self.logger.info("********Test_003_AddCustomer*******")
        self.driver=setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*****LoginSuccessful*****")
        self.logger.info("*******Started adding customer info**********")
        self.addCust = AddCustomer(self.driver)
        self.addCust.clickOnCustomersMenu()
        self.addCust.clickOnCustomersMenuItem()
        self.addCust.clickOnAddNew()
        self.logger.info("********Providing Customer Info******")
        self.email = random_generator() + "@gmail.com"
        self.addCust.setEmail(self.email)
        self.addCust.setPassword("test123")
        self.addCust.setFirstName("Ravi")
        self.addCust.setlastName("Kumar")
        self.addCust.setGender("Male")
        self.addCust.setDOB("7/2/1999")
        self.addCust.setCompanyName("STAR")
        self.addCust.setNewsletter("Test store 2")
        #self.addCust.chktaxexcept_id()
        self.addCust.setCustomerRoles("Guests")
        self.addCust.setmanagerOfVendor("Vendor 2")



        self.addCust.setAdminContent("aaa bbbbbbb ccccccccccccc dddddddddd")
        #self.addCust.clickonsave()

        self.logger.info("*******8saving Customer info******")
        self.logger.info("***** Add Customer Validation*****")
        self.msg = self.driver.find_element_by_tag_name("body").text
        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("**** Add Customer Test passed")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_addCustomer_scr.png")
            self.logger.error("*******8AddCustomer Test Failed*********")
            assert False == False
        self.driver.close()
        self.logger.info("*********Ending Home page title test******8")

def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))