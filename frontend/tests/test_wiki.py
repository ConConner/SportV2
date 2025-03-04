from time import sleep
import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoAlertPresentException, ElementClickInterceptedException

class wiki_test(unittest.TestCase):

    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("window.scrollBy(0, -100);")  # Scroll up 100 pixels


    def setUp(self):
        # Set Chrome options and preferences
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")  # Run in headless mode
        chrome_options.add_argument("--disable-gpu")
        
        # Initialize the WebDriver with the options
        self.driver = webdriver.Chrome(options=chrome_options)
        
        # Navigate to your target URL but fail the test if it takes too long
        self.driver.set_page_load_timeout(100)
        
    def test_nav_menu(self):
        self.driver.get("http://localhost:3000")
        self.sites =[["Startseite", "/"], ["Testseite", "/test_page"],["Wiki-Seite", "/wiki_page"]]
        for thing in self.sites:
            # Find the link to the page
            link = self.driver.find_element(By.LINK_TEXT, thing[0])
            link.click()
            sleep(1)
            self.assertEqual(self.driver.current_url, "http://localhost:3000"+thing[1], "The link did not lead to the right page!")
            print("Navigated to "+thing[0]+"!")

    def test_wiki_page(self):
        # Find the link to the page
        self.driver.get("http://localhost:3000/wiki_page")
        self.sites =[["Ansicht von Leistungen und Ergebnissen pro Athlet und Disziplin", "#leistungen_ergebnisse_athlet_diziplin"], ["Detailansicht eines Athleten","#detailansicht_athleten"],
                     ["Eintragsmodus für Leistungswerte","#eintragsmodus_leistungen"], ["Erstellen oder Ändern von Reglungen","#erstellen_ändern_von_reglungen"],
                     ["Export eines Athleten","#export_eines_athleten"],["Export eines Athleten und seiner Daten als PDF","#export_eines_athleten_pdf"],
                     ["Export mehrerer Athleten als CSV","#export_mehrer_athlethen"],["Liste aller Athleten","#liste_athlethen"], 
                     ["Manuelle Aktualisierung der Reglungen durch Knopfdruck","#knopf_reglungsaktualisierung"],["Medaillen Ansicht","#medaillen_ansicht"], ["Regelungsverwaltung","#regelungsverwaltung"],
                     ["Visuelle Darstellung der Entwicklung eines Athleten","#visuelle_darstellung_entwicklung"]]
        for thing in self.sites:
            # Find the link to the page
            link = self.driver.find_element(By.XPATH, f'//a[@href="{thing[1]}"]')
            self.scroll_into_view(link)  # Scroll to the element
            sleep(1)  # Wait for the scroll to complete
            try:
                link.click()
            except ElementClickInterceptedException:
                self.driver.execute_script("window.scrollBy(0, -100);")  # Scroll up a bit and try again
                sleep(1)
                link.click()
            sleep(1)
            self.assertEqual(self.driver.current_url, "http://localhost:3000/wiki_page"+thing[1], "The link did not lead to the right page!")
            print("Navigated to "+thing[0]+"!")

    def tearDown(self):
        # Close the browser
        self.driver.quit()
        print("Test Wiki Success!")

if __name__ == "__main__":
    unittest.main()