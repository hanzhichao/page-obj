from time import sleep
from .function import insert_img
import unittest
from .driver import chrome


class MyTest(unittest.TestCase):

    def setUp(self):
        self.driver = chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

