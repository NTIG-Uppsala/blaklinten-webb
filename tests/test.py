import time
from os import getcwd, path
from unittest import TestCase, main

from selenium import webdriver
from selenium.webdriver.common.by import By


class Tests(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome()

    def setUp(self):
        self.browser.get(path.join(getcwd(), "index.html"))

    def tearDown(self):
        _ = self.browser.get_log("browser")
        self.browser.get("about:blank")

    def testNoErrors(self):
        log = self.browser.get_log("browser")
        for message in log:
            self.assertNotEqual(message["level"], "SEVERE")

    def testCompanyNamePresent(self):
        self.assertIn("Florist Blåklinten", self.browser.page_source)

    def testFooter(self):
        self.browser.find_element(By.TAG_NAME, "footer")

    def scrollToBottom(self):
        time.sleep(1)
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

    def testInstagramLink(self):
        self.scrollToBottom()
        self.browser.find_element(By.ID, "instagram-link").click()
        self.assertEqual(
            "https://www.instagram.com/ntiuppsala/", self.browser.current_url
        )

    def testTwitterLink(self):
        self.scrollToBottom()
        self.browser.find_element(By.ID, "x-link").click()
        self.assertIn("https://twitter.com", self.browser.current_url)
        self.assertIn("ntiuppsala", self.browser.current_url)

    def testFacebookLink(self):
        self.scrollToBottom()
        self.browser.find_element(By.ID, "facebook-link").click()
        self.assertIn("https://www.facebook.com/ntiuppsala", self.browser.current_url)

    def testPhoneNumberPresent(self):
        phone_number_links = self.browser.find_elements(
            By.XPATH, "//a[@href='tel:0630-555-555']"
        )
        for phone_number_link in phone_number_links:
            self.assertIn("0630-555-555", phone_number_link.text)

    def testEmailAddressPresent(self):
        email_address_links = self.browser.find_elements(
            By.XPATH, "//a[@href='mailto:info@ntig-uppsala.github.io']"
        )
        for email_address_link in email_address_links:
            self.assertIn("info@ntig-uppsala.github.io", email_address_link.text)

    def testAddressPresent(self):
        self.assertIn("Fjällgatan 32H", self.browser.page_source)
        self.assertIn("981 39 Kiruna", self.browser.page_source)

    def testOpeningHoursPresent(self):
        self.assertIn("Öppettider", self.browser.page_source)
        self.assertIn("Måndag-fredag 10:00-16:00", self.browser.page_source)
        self.assertIn("Lördag 12:00-15:00", self.browser.page_source)

    def currentlyOpenHelper(self, date_string: str, expected_result: str):
        self.browser.execute_script(f'updateCurrentlyOpen(new Date("{date_string}"));')
        self.assertIn(expected_result, self.browser.page_source)

    def testCurrentlyOpen(self):
        open_text = "Just nu har vi öppet"
        closed_text = "Vi öppnar klockan"

        # Monday
        self.currentlyOpenHelper("2023-09-04T09:59:00", closed_text + " 10 idag")
        self.currentlyOpenHelper("2023-09-04T10:00:00", open_text)
        self.currentlyOpenHelper("2023-09-04T15:59:00", open_text)
        self.currentlyOpenHelper("2023-09-04T16:00:00", closed_text + " 10 imorgon")

        # Friday
        self.currentlyOpenHelper("2023-09-08T09:59:00", closed_text + " 10 idag")
        self.currentlyOpenHelper("2023-09-08T10:00:00", open_text)
        self.currentlyOpenHelper("2023-09-08T15:59:00", open_text)
        self.currentlyOpenHelper("2023-09-08T16:00:00", closed_text + " 12 imorgon")

        # Saturday
        self.currentlyOpenHelper("2023-09-09T11:59:00", closed_text + " 12 idag")
        self.currentlyOpenHelper("2023-09-09T12:00:00", open_text)
        self.currentlyOpenHelper("2023-09-09T14:59:00", open_text)
        self.currentlyOpenHelper("2023-09-09T15:00:00", closed_text + " 10 på måndag")

        # Sunday
        self.currentlyOpenHelper("2023-09-10T13:00:00", closed_text + " 10 imorgon")

        # Closed days
        self.currentlyOpenHelper("2023-01-01T13:00:00", closed_text + " 10 imorgon")
        self.currentlyOpenHelper("2023-01-06T13:00:00", closed_text + " 12 imorgon")
        self.currentlyOpenHelper("2023-12-24T13:00:00", closed_text + " 10 på onsdag")

        # Following test only tests dates in 2023 and may not be the same every year
        self.currentlyOpenHelper("2023-04-30T13:00:00", closed_text + " 10 på tisdag")

    def testClosedDaysPresent(self):
        closed_days = [
            ("Nyårsdagen", "1/1"),
            ("Trettondedag jul", "6/1"),
            ("Första maj", "1/5"),
            ("Sveriges nationaldag", "6/6"),
            ("Julafton", "24/12"),
            ("Juldagen", "25/12"),
            ("Annandag jul", "26/12"),
            ("Nyårsafton", "31/12"),
        ]
        self.assertIn("Stängda dagar", self.browser.page_source)

        opening_hour_list = self.browser.find_element(By.ID, "opening-hours")
        for closed_day in closed_days:
            self.assertIn(closed_day[0], opening_hour_list.text)
            self.assertIn(closed_day[1], opening_hour_list.text)

    def testFonts(self):
        h1_font = self.browser.find_element(By.CLASS_NAME, "h1")
        self.assertEqual(
            h1_font.value_of_css_property("font-family"), '"DM Serif Display"'
        )
        p_fonts = self.browser.find_elements(By.TAG_NAME, "p")
        for p_font in p_fonts:
            self.assertEqual(p_font.value_of_css_property("font-family"), "Assistant")

    def testFavicon(self):
        self.browser.find_element(By.XPATH, ".//link[@rel='shortcut icon']")

    def testLogo(self):
        src = self.browser.find_element(
            By.XPATH, "//a[@class='navbar-brand']/img"
        ).get_attribute("src")
        self.assertIn(".svg", src)


if __name__ == "__main__":
    main(verbosity=2)
