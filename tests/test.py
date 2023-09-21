import time
from os import getcwd, path
from unittest import TestCase, main

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class Tests(TestCase):
    doNotCloseBrowser = True
    hideWindow = False

    @classmethod
    def setUpClass(cls):
        chr_options = Options()

        if cls.doNotCloseBrowser:
            chr_options.add_experimental_option("detach", True)

        if cls.hideWindow:
            chr_options.add_argument("--headless")

        cls.browser = webdriver.Chrome(options=chr_options)

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
        self.assertIn("Måndag-fredag", self.browser.page_source)
        self.assertIn("Lördag", self.browser.page_source)
        self.assertIn("Söndag", self.browser.page_source)

    def currentlyOpenHelper(self, date_string: str, expected_result: str):
        self.browser.execute_script(f'updateCurrentlyOpen(new Date("{date_string}"));')
        self.assertIn(expected_result, self.browser.page_source)

    def testCurrentlyOpen(self):
        open_text = "Just&nbsp;nu:&nbsp;"  # Only shows when store is open
        # The following code snippet shows when store is not open
        opening10Today_text = "Vi öppnar klockan 10"
        opening10Tomorow_text = "Vi öppnar klockan 10 imorgon"

        opening12Today_text = "Vi öppnar klockan 12"
        opening12Tomorow_text = "Vi öppnar klockan 12 imorgon"

        openingMonday_text = "Vi öppnar klockan 10 på måndag"

        openignTuseday_text = "Vi öppnar klockan 10 på tisdag"

        openingWendsday_text = "Vi öppnar klockan 10 på onsdag"

        # Monday
        self.currentlyOpenHelper("2023-09-04T09:59:00", opening10Today_text)
        self.currentlyOpenHelper("2023-09-04T10:00:00", open_text)
        self.currentlyOpenHelper("2023-09-04T15:59:00", open_text)
        self.currentlyOpenHelper("2023-09-04T16:00:00", opening10Tomorow_text)

        # Friday
        self.currentlyOpenHelper("2023-09-08T09:59:00", opening10Today_text)
        self.currentlyOpenHelper("2023-09-08T10:00:00", open_text)
        self.currentlyOpenHelper("2023-09-08T15:59:00", open_text)
        self.currentlyOpenHelper("2023-09-08T16:00:00", opening12Tomorow_text)

        # Saturday
        self.currentlyOpenHelper("2023-09-09T11:59:00", opening12Today_text)
        self.currentlyOpenHelper("2023-09-09T12:00:00", open_text)
        self.currentlyOpenHelper("2023-09-09T14:59:00", open_text)
        self.currentlyOpenHelper("2023-09-09T15:00:00", openingMonday_text)

        # Sunday
        self.currentlyOpenHelper("2023-09-10T13:00:00", opening10Tomorow_text)

        # Closed days
        self.currentlyOpenHelper("2023-01-01T13:00:00", opening10Tomorow_text)
        self.currentlyOpenHelper("2023-01-06T13:00:00", opening12Tomorow_text)
        self.currentlyOpenHelper("2023-12-24T13:00:00", openingWendsday_text)
        self.currentlyOpenHelper("2023-04-30T13:00:00", openignTuseday_text)

    def testClosedDaysPresent(self):
        # Days in closed days list
        self.assertIn("Juldagen", self.browser.page_source)
        self.assertIn("Första maj", self.browser.page_source)
        self.assertIn("Julafton", self.browser.page_source)
        self.assertIn("Nyårsafton", self.browser.page_source)
        # Numbers in closed days list
        self.assertIn("1/1", self.browser.page_source)
        self.assertIn("6/6", self.browser.page_source)
        self.assertIn("25/12", self.browser.page_source)
        self.assertIn("31/12", self.browser.page_source)

    def testFonts(self):
        h1_font = self.browser.find_element(By.CLASS_NAME, "h1")
        self.assertTrue(
            h1_font.value_of_css_property("font-family").startswith(
                '"DM Serif Display"'
            )
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
