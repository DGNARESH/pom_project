import unittest
from selenium import webdriver
import HtmlTestRunner
from Excellsheets import XLutilities
import openpyxl
import time
import sys
sys.path.append("C:/Users/dgsai/PycharmProjects/pom_project/pageobject")

from pageobject.login import login
#from pageobject.login import login

class loginTest(unittest.TestCase):
    baseURL = 'https://demo.nopcommerce.com/'  #"https://demo.nopcommerce.com/login?returnUrl=%2F"
    #username ="admin1@yourstore.com"
    #password ="admin@123"
    path = "..\\Excellsheets\\inputs.xlsx"
    rows = XLutilities.getRowcount(path, 'Sheet1')

    username = XLutilities.readdata(path, 'Sheet1', 2, 1)
    password = XLutilities.readdata(path, 'Sheet1', 2, 2)
    driver = webdriver.Chrome(executable_path="..\\Driver\\chromedriver.exe")

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    def test_loginpage(self):
        lp = login(self.driver)
        lp.clicklogin1()
        time.sleep(5)
        lp.setusername(self.username)
        lp.setpassword(self.password)
        lp.clicklogin()
        lp.clicklogout()
        time.sleep(5)

        if self.assertEqual("nopCommerce demo store",self.driver.title,"not matched"):
            XLutilities.writtenData(self.path, 'Sheet1', 2, 3, 'PASS')
        else:  #self.assertNotEqual("nopCommerce demo store", self.driver.title, "not matched")
            XLutilities.writtenData(self.path, 'Sheet1', 3, 2, 'FAIL')


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="..\\Reports"))

