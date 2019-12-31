import unittest
from selenium import webdriver
import page

class OrderDresses(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://automationpractice.com/')
        self.driver.maximize_window()

    def test_order_dresses(self):
        dresses = page.Page(self.driver)
        dresses.order_dresses()

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
