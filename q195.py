# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("https://list1.mysteel.com/price/p-10018--010211--1.html")
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='注册'])[1]/preceding::span[1]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='注册'])[1]/following::input[1]").clear()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='注册'])[1]/following::input[1]").send_keys("webhao1230")
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='注册'])[1]/following::input[2]").clear()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='注册'])[1]/following::input[2]").send_keys("fang933934")
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='注册'])[1]/following::div[8]").click()
        time.sleep(5)
        ul = driver.find_element_by_css_selector("ul.nlist")
        lis = ul.find_elements_by_xpath('li')

        for x in lis:
            flag=AppDynamicsJob.isElementExist(self,x)
            if flag:
                print(x.find_element_by_xpath('span').text)
                print(x.find_element_by_xpath('a').get_attribute('href'))

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.assertEqual([], self.verificationErrors)

    def isElementExist(self, element):
        flag = True
        try:
            element.find_element_by_xpath('span')
            return flag

        except:
            flag = False
            return flag

if __name__ == "__main__":
    unittest.main()
