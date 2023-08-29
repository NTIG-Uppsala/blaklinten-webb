from os import path, getcwd
from unittest import TestCase, main

from selenium import webdriver

class Tests(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.browser.get(path.join(getcwd(), "index.html"))

    def tearDown(self):
        self.browser.get('about:blank')

    def test_company_name_present(self):
        self.assertIn("Florist Blåklinten", self.browser.page_source)

if __name__ == '__main__':
    main(verbosity=2)