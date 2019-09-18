# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from group import Group
from application import Applicaton

class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.app = Applicaton()

    
    def test_add_group(self):
        self.app.login(username="admin", password="secret")
        self.app.create_group(Group(name="group_name", header="group_header", footer="group_footer"))
        self.app.logout()

    def test_add_empty_group(self):
        self.app.login(username="admin", password="secret")
        self.app.create_group(Group(name="", header="", footer=""))
        self.app.logout()



    
    def tearDown(self):
        self.app.destroy()

if __name__ == "__main__":
    unittest.main()
