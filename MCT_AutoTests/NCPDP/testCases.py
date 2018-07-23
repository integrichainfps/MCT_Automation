import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class TestNewNCPDP(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        _login(self)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_ncpdp_new(self):
        _getNCPDPPage(self)
        driver = self.driver
        newNcpdpButton = driver.find_element_by_xpath("//div[contains(@class,'tool-button') and contains(@class,'add-button')]/div[@class='button-outer']/span[@class='button-inner']")
        newNcpdpButton.click()

    def tearDown(self):
        self.driver.quit()


def _login(self):
    self.driver.implicitly_wait(10)
    self.base_url = "https://dev-mct-claimtrak.integrichain.net/"
    self.driver.get(self.base_url)
    username = self.driver.find_element_by_id('MCTApplication_Membership_LoginPanel0_Username')
    password = self.driver.find_element_by_id('MCTApplication_Membership_LoginPanel0_Password')
    username.send_keys('admin')
    password.send_keys('password')
    self.driver.find_element_by_id('MCTApplication_Membership_LoginPanel0_LoginButton').click()

def _getNCPDPPage(self):
    self.driver.implicitly_wait(10)
    ncpdpd = self.driver.find_element_by_link_text('Ncpdp Hd')
    ncpdpd.click()

if __name__ == "__main__":
    unittest.main()
