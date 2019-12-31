import unittest
from selenium import webdriver
import time
import xpaths


class OrderItem(unittest.TestCase):


    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.get('http://automationpractice.com/')
        self.driver.maximize_window()
        self.driver.find_element_by_xpath(xpaths.scroller).click()
        self.driver.execute_script('window.scrollTo(0, 1080)')
        self.driver.execute_script("window.scrollTo(1080, 0)")

    def test_order_item(self):
        #Allgemein Class Array
        main_Class = self.driver.find_elements_by_xpath(xpaths.product_id)
        print(main_Class)
        print(len(main_Class))

        #Price Array
        test =list()
        Price =list()
        for i in range(1, len(main_Class)):
            test.append(xpaths.apend_1 + str(i) + xpaths.apend_2)
            Price.append(self.driver.find_element_by_xpath('' + test[i - 1] + '').text)
        for item in Price:
            #print(Price.index(item)+1, item)
            #print(Price)
            #print("Teuerste Kleid  is:", max(Price))
            time.sleep(3)

            #Hochste Price
        for i in range(1, len(Price)):
            if Price[i - 1] == max(Price):
                self.driver.find_element_by_xpath(xpaths.highest_price_1 + str(i) + xpaths.highest_price_2).click()
            time.sleep(3)
        self.driver.find_element_by_xpath(xpaths.cloth_colour).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(xpaths.cloth_size).send_keys("L")
        time.sleep(3)
        self.driver.find_element_by_xpath(xpaths.add_to_cart).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(xpaths.proceed_to_checkout).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(xpaths.product_quantity).click()

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()