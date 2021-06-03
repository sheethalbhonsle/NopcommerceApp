import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:

        baseURL = ReadConfig.getApplicationURL()
        username = ReadConfig.getUseremail()
        password = ReadConfig.getPassword()
        logger = LogGen.loggen()
        def test_homePageTitle(self,setup):
            self.logger.info("***Test_001_Login***")
            self.logger.info("***Verifying Home Page Title**")
            self.driver = setup
            self.driver.get(self.baseURL)
            act_title=self.driver.title

            if act_title == "Your store. Login":
                assert True
                # browser is closed
                self.driver.close()
                self.logger.info("***Home Page Title Test is Passed***")
            else:
                self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
                self.driver.close()
                self.logger.error("***Home Page Title Test is Failed***")
                assert False
        def test_login(self,setup):
            self.logger.info("***Verifying Login Test***")
            self.driver = setup
            self.driver.get(self.baseURL)
            #create an object for loginpage
            self.lp = LoginPage(self.driver)
            #by using object(lp) we can access the all the methods
            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            act_title = self.driver.title
            #self.driver.close()
            if act_title == "Dashboard / nopCommerce administration":
                assert True
                self.logger.info("***Login Test is Passed***")
                self.driver.close()
            else:
                self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
                self.logger.error("***Login Test is Failed***")
                self.driver.close()
                assert False

