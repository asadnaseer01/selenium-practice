import unittest
from selenium import webdriver
import xpaths
import page

class OrderItem(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://automationpractice.com/')
        self.driver.maximize_window()
        page.Page(self.driver).scroll_down()

    def test_order_item(self):
        order = page.Page(self.driver)
        order.order_item()

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
