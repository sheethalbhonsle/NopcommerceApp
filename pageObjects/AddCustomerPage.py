import time
from selenium.webdriver.support.ui import Select

class AddCustomer():
    #lnkCustomers_menu_xpath = "//a[@href='#']//span[contain(text(),'Customers')]"
    #lnkCustomers_menu_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a/p"
    lnkCustomers_menu_xpath = "//p[contains(text(),'Customers')]"
    #lnkCustomers_menuitem_xpath = "//span[@class='menu-item-title'][contains(text(),'Customer')]"
    lnkCustomers_menuitem_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p"

    #btnAddnew_xpath = "//a[@class='btn bg-blue']"
    btnAddnew_xpath = "/html/body/div[3]/div[1]/form[1]/div/div/a"
    #btnAddnew_xpath = "//*[contains(text(),'Add new')]"
    txtEmail_id = "Email"
    txtPassword_id = "Password"
    txtFirstName_id = "FirstName"
    txtLastName_id = "LastName"
    rdMaleGender_id = "Gender_Male"
    rdFemaleGender_id = "Gender_Female"
    txtDob_id = "DateOfBirth"
    txtCompName_id = "Company"
    #chktaxexcept_id = "IsTaxExempt"
    drpdivnewsletter_xpath = "//*[@id='customer-info']/div[2]/div[9]/div[2]/div/div[1]/div/div"

    #drpUrstorename_xpath = "//*[@id='SelectedNewsletterSubscriptionStoreIds_taglist']/li/span[1]"
    drpUrstorename_xpath = "//*[@id='SelectedNewsletterSubscriptionStoreIds_listbox']/li[1]"
    drpTeststore2_xpath = "//*[@id='SelectedNewsletterSubscriptionStoreIds_listbox']/li[2]"

    #drpNewsletter_id = "//*[@id='customer-info']/div[2]/div[9]/div[2]/div/div[1]/div/div"

    txtcustomerRoles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    lstitemAdministrators_xpath ="//li[contains(text(),'Administrators')]"
    #lstitemAdministrators_xpath = "//*[@id='SelectedCustomerRoleIds_taglist']/li[2]/span[1]"
    lstitemForumModerators_xpath = "//li[contains(text(),'Forum Moderators')]"
    lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstitemGuests_xpath = "//li[contains(text(),'Guests')]"

    lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"

    drpmgrOfVendor_xpath = "//select[@id='VendorId']"
    txtadminComment_id = "AdminComment"
    #btnSave_xpath = "//button[@name='save']"

    def __init__(self,driver):
        self.driver = driver
    def clickOnCustomersMenu(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menu_xpath).click()
    def clickOnCustomersMenuItem(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menuitem_xpath).click()
    def clickOnAddNew(self):
        self.driver.find_element_by_xpath(self.btnAddnew_xpath).click()
    def setEmail(self,email):
        self.driver.find_element_by_id(self.txtEmail_id).send_keys(email)
    def setPassword(self,password):
        self.driver.find_element_by_id(self.txtPassword_id).send_keys(password)
    def setFirstName(self,fname):
        self.driver.find_element_by_id(self.txtFirstName_id).send_keys(fname)
    def setlastName(self,lname):
        self.driver.find_element_by_id(self.txtLastName_id).send_keys(lname)
    def setDOB(self,dob):
        self.driver.find_element_by_id(self.txtDob_id).send_keys(dob)
    def setCompanyName(self,compname):
        self.driver.find_element_by_id(self.txtCompName_id).send_keys(compname)
    #def settaxexempt(self):
    #    self.driver.find_element_by_id(self.chktaxexcept_id).click()

    def setNewsletter(self,news):
        self.driver.find_element_by_xpath(self.drpdivnewsletter_xpath).click()
        time.sleep(3)
        if news == 'Your store name':
            self.listitems = self.driver.find_element_by_xpath(self.drpUrstorename_xpath).click()
        elif news == 'Test store 2':
            self.listitems = self.driver.find_element_by_xpath(self.drpTeststore2_xpath).click()
        else:
            self.listitems = self.driver.find_element_by_xpath(self.drpTeststore2_xpath).click()
        #    self.driver.execute_scripts("arguments[0].click(),",self.listitems)

    #def setCustomerRole(self,role):
    #    self.driver.find_element_by_xpath(self.txtcustomerRoles_xpath).click()
     #   time.sleep(3)
     #   if role == 'Registered':
     #       self.listitem =self.driver.find_element_by_xpath(self.lstitemRegistered_xpath).click()
     #   elif role == 'Administrators':
     #       self.listitem= self.driver.find_element_by_xpath(self.lstitemAdministrators_xpath)
      #  elif role == 'Guests':
      #      self.listitem= self.driver.find_element_by_xpath(self.lstitemGuest_xpath)
     #       time.sleep(3)
     #   else:
     #       self.listitem= self.driver.find_element_by_xpath(self.lstitemvendors_xpath)
      #  time.sleep(3)
        #self.driver.execute_scripts("arguments[0].click();",self.listitem)

    def setCustomerRoles(self, role):
        self.driver.find_element_by_xpath(self.txtcustomerRoles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemAdministrators_xpath)
        elif role == 'Guests':
            # Here user can be Registered( or) Guest, only one
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element_by_xpath(self.lstitemGuests_xpath)
        elif role == 'Registered':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemVendors_xpath)
        else:
            self.listitem = self.driver.find_element_by_xpath(self.lstitemGuests_xpath)
        time.sleep(3)
        # self.listitem.click()
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setmanagerOfVendor(self,value):
        drp=Select(self.driver.find_element_by_xpath(self.drpmgrOfVendor_xpath))
        drp.select_by_visible_text(value)

    def setGender(self,gender):
        if gender =='Male':
            self.driver.find_element_by_id(self.rdMaleGender_id).click()
        elif gender == 'Female':
            self.driver.find_element_by_id(self.rdFemaleGender_id).click()
        else:
            self.driver.find_element_by_id(self.rdMaleGender_id).click()
    def setAdminContent(self,content):
        self.driver.find_element_by_id(self.txtadminComment_id).send_keys(content)
    #def clickonsave(self):
     #   self.driver.find_element_by_xpath(self.btnSave_xpath).click()

