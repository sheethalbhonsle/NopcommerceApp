import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtiles
import time
#https://www.youtube.com/watch?v=879YnSl80b0    (video DDT)

class Test_002_DDT_Login:

        baseURL = ReadConfig.getApplicationURL()
        path=".//TestData/LoginData.xlsx"
        #data is coming from xlsx file not from ini file
        #username = ReadConfig.getUseremail()
        #password = ReadConfig.getPassword()
        logger = LogGen.loggen()

        def test_login_ddt(self,setup):
            self.logger.info("*****Test_002_DDT_Login******* ")
            self.logger.info("***Verifying Login DDT Test***")
            self.driver = setup
            self.driver.get(self.baseURL)
            #create an object for loginpage
            self.lp = LoginPage(self.driver)

            self.rows=XLUtiles.getRowCount(self.path,'Sheet1')
            print("Number of rows in a Excel:", self.rows)

            lst_status=[] #empty list

            for r in range(2,self.rows+1):
                self.user= XLUtiles.readData(self.path,'Sheet1',r,1)
                self.password = XLUtiles.readData(self.path, 'Sheet1', r, 2)
                self.expected = XLUtiles.readData(self.path, 'Sheet1', r, 3)
                self.lp.setUserName(self.user)
                self.lp.setPassword(self.password)
                self.lp.clickLogin()
                time.sleep(5)
                act_title=self.driver.title
                exp_title="Dashboard / nopCommerce administration"

                if act_title==exp_title:
                    if self.expected=="Pass":
                        self.logger.info("*****Passed****")
                        self.lp.clickLogout();
                        lst_status.append("Pass")
                    elif self.expected=="Fail":
                        self.logger.info("****Fail***")
                        self.lp.clickLogout();
                        lst_status.append("Fail")
                elif act_title!=exp_title:
                    if self.expected=="Pass":
                        self.logger.info("********Failed**")
                        lst_status.append("Fail")
                    elif self.expected=="Fail":
                        self.logger.info("****Pass****")
                        lst_status.append("Pass")
            if "Fail" not in lst_status:
                self.logger.info("****Login DDT test passed***")
                self.driver.close()
                assert True
            else:
                self.logger.info("****Login DDT test failed***")
                assert False

            self.logger.info("*******End of Login DDT Test")
            self.logger.info("****Completed TC_LoginDDT_002****")




