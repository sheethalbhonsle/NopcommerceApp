class LoginPage():
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_tagname = "button"
    link_logout_linktext="Logout"

    def __init__(self,driver):
        self.driver = driver
    def setUserName(self,username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)
        print("Username is sent.....")


    def setPassword(self,password):
        print("Code has executed till here ************")
        print("Entering password id:", self.textbox_password_id)
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_tag_name(self.button_login_tagname).click()

    def clickLogout(self):
        print("link is clicked")
        self.driver.find_element_by_link_text(self.link_logout_linktext).click()