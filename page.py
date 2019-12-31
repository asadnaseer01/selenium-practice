import time

from selenium.webdriver import ActionChains

import xpaths
import unittest


class Page:

    def __init__(self, driver):
        self.driver = driver

    def order_item(self):
        items = self.get_items()
        self.select_item(items)
        self.order_details()

    def get_items(self):

        main_Class = self.driver.find_elements_by_xpath(xpaths.product_id)
        # unittest.TestCase.assertEqual(len(main_Class), 7)
        # Price Array
        test = list()
        price = list()
        for i in range(1, len(main_Class)):
            test.append(xpaths.apend_1 + str(i) + xpaths.apend_2)
            price.append(self.driver.find_element_by_xpath('' + test[i - 1] + '').text)
            time.sleep(3)

        return price

        # Hochste Price

    def select_item(self, price):
        for i in range(1, len(price)):
            if price[i - 1] == max(price):
                self.driver.find_element_by_xpath(xpaths.highest_price_1 + str(i) + xpaths.highest_price_2).click()
                time.sleep(3)

    def order_details(self):
        elem = self.driver.find_element_by_xpath(xpaths.cloth_colour)
        elem.click()
        time.sleep(3)
        self.driver.find_element_by_xpath(xpaths.cloth_size).send_keys("L")
        time.sleep(3)
        self.driver.find_element_by_xpath(xpaths.add_to_cart).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(xpaths.proceed_to_checkout).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(xpaths.product_quantity).click()

    def order_dresses(self):

        # self.driver.find_element_by_xpath(xpaths.dresses)
        actions = ActionChains(self.driver)
        dresses_tab = self.driver.find_element_by_xpath(xpaths.dresses_tab)
        dresses_element = self.driver.find_element_by_xpath(xpaths.dresses)
        actions.move_to_element(dresses_tab)
        actions.click(dresses_element)
        actions.perform()
        time.sleep(3)
        self.scroll_down()
        time.sleep(2)
        actions = ActionChains(self.driver)
        dresses_image = self.driver.find_element_by_xpath(xpaths.dress_image)
        dresses_click = self.driver.find_element_by_xpath(xpaths.dress_click)
        actions.move_to_element(dresses_image)
        actions.click(dresses_click)
        actions.perform()
        time.sleep(3)
        self.driver.find_element_by_xpath(xpaths.cloth_size).send_keys("M")
        time.sleep(3)
        self.driver.find_element_by_xpath(xpaths.dress_clr).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(xpaths.add_to_cart).click()
        time.sleep(3)

    def order_tshirts(self):
        actions = ActionChains(self.driver)
        tshirts_tab = self.driver.find_element_by_xpath(xpaths.tshirts_tab)
        tshirts_element = self.driver.find_element_by_xpath(xpaths.tshirts)
        actions.move_to_element(tshirts_tab)
        actions.click(tshirts_element)
        actions.perform()
        time.sleep(3)

        actions = ActionChains(self.driver)
        shirt_image = self.driver.find_element_by_xpath(xpaths.shirt_image)
        shirt_click = self.driver.find_element_by_xpath(xpaths.shirt_click )
        actions.move_to_element(shirt_image)
        actions.click(shirt_click)
        actions.perform()
        time.sleep(3)

        self.driver.find_element_by_xpath(xpaths.cloth_size).send_keys("M")
        time.sleep(3)
        self.driver.find_element_by_xpath(xpaths.dress_clr).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(xpaths.add_to_cart).click()
        time.sleep(3)
    def scroll_down(self):
        #self.driver.find_element_by_xpath(xpaths.scroller).click()
        self.driver.execute_script('window.scrollTo(0, 1080)')
        self.driver.execute_script("window.scrollTo(1080, 0)")
