class login():
    #locaters of all elements

    textbox_username_name = "Email"
    textbox_password_name = "Password"
    button_login1_xpath = '/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[2]/a'
    button_login_xpath = '/html/body/div[6]/div[3]/div/div/div/div[2]/div[1]/div[2]/form/div[3]/input'
    log_out_xpath = '/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[2]/a'


    #constructor
    def __init__(self,driver):
        self.driver = driver

    def setusername(self,username):
        self.driver.find_element_by_name(self.textbox_username_name).send_keys(username)

    def setpassword(self,password):
        self.driver.find_element_by_name(self.textbox_password_name).send_keys(password)

    def clicklogin1(self):
        self.driver.find_element_by_xpath(self.button_login1_xpath).click()

    def clicklogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clicklogout(self):
        self.driver.find_element_by_xpath(self.log_out_xpath).click()

