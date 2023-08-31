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
        self.browser.find_element(By.TAG_NAME, "footer")
    
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

    def test_phone_number_present(self):
        phone_number_link = self.browser.find_element(By.XPATH, "//a[@href='tel:0630-555-555']")
        self.assertIn("0630-555-555", phone_number_link.text)
    
    def test_email_address_present(self):
        email_address_link = self.browser.find_element(By.XPATH, "//a[@href='mailto:info@ntig-uppsala.github.io']")
        self.assertIn("info@ntig-uppsala.github.io", email_address_link.text)

    def test_address_present(self):
        self.assertIn("Fjällgatan 32H", self.browser.page_source)
        self.assertIn("981 39 Kiruna", self.browser.page_source)

    def test_opening_hours_present(self):
        self.assertIn("Öppettider", self.browser.page_source)
        self.assertIn("Måndag-fredag 10:00-16:00", self.browser.page_source)
        self.assertIn("Lördag 12:00-15:00", self.browser.page_source)

    def test_closed_days_present(self):
        self.assertIn("Stängda dagar", self.browser.page_source)
    
if __name__ == '__main__':
    main(verbosity=2)