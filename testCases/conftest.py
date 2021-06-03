from selenium import webdriver
import pytest
#C:\Users\Heman\AppData\Local\Programs\Python\Python39\Scripts tokeep browser exe file
#https://github.com/mozilla/geckodriver/releases
@pytest.fixture()
def setup(browser):
    #set up method will decide which browser will launch
    if browser=='chrome':
        driver=webdriver.Chrome()
        print("launching chrome browser.........")
    elif browser=='firefox':
        driver=webdriver.Firefox()
        print("launching firefox browser...........")
    return driver
#this will get the value from CLI/hooks(command line interface)
# #broser name is passed through command prompt
def pytest_addoption(parser):
    parser.addoption("--browser")
@pytest.fixture()
def browser(request):#return the browser value to setup method
    return request.config.getoption("--browser")
########## Pytest HTML Report#########

#it is hook for adding environment info to HTML report
def pytest_configure(config):
    config._metadata['Project Name']= 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'sheetal'
#it is hook for delete/modify environment info to HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)