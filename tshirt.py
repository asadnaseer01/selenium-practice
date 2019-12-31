import unittest
from selenium import webdriver
import page

class OrderTshirts(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://automationpractice.com/')
        self.driver.maximize_window()

    def test_order_tshirts(self):
        tshirts = page.Page(self.driver)
        tshirts.order_tshirts()

    def tearDown(self):
        self.driver.close()

    if __name__ == '__main__':
        unittest.main()