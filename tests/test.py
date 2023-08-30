from os import path, getcwd
from unittest import TestCase, main

from selenium import webdriver
from selenium.webdriver.common.by import By

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

    def test_footer(self):
        footer = self.browser.find_element(By.TAG_NAME, "footer")
    
    def test_instagram_link(self):
        self.browser.find_element(By.ID, "instagram-link").click()
        self.assertEqual("https://www.instagram.com/ntiuppsala/", self.browser.current_url)

    def test_twitter_link(self):
        self.browser.find_element(By.ID, "x-link").click()
        self.assertIn("https://twitter.com", self.browser.current_url)
        self.assertIn("ntiuppsala", self.browser.current_url)

    def test_facebook_link(self):
        self.browser.find_element(By.ID, "facebook-link").click()
        self.assertEqual("https://www.facebook.com/ntiuppsala", self.browser.current_url)


if __name__ == '__main__':
    main(verbosity=2)