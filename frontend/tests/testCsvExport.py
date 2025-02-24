from time import sleep
import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoAlertPresentException


class BasicSeleniumTest(unittest.TestCase):    
    
    def extract_digits_until_non_digit(self, input_string):
        """
        Extracts all consecutive digits from the start of the string
        until the first non-digit character is encountered.
        
        :param input_string: The input string to process
        :return: A string of digits found at the start of the input or an empty string if none
        """
        result = ''
        for char in input_string:
            if char.isdigit():
                result += char
            else:
                break
        return result
    
    def delete_files_in_directory(self, directory_path):
        try:
            files = os.listdir(directory_path)
            for file in files:
                file_path = os.path.join(directory_path, file)
                if os.path.isfile(file_path):
                    os.remove(file_path)
            print("All files deleted successfully.")
        except OSError:
            print("Error occurred while deleting files.")
    
    def setUp(self):
        # Define the download directory
        self.download_dir = os.path.abspath("test_download_dir")
        if not os.path.exists(self.download_dir):
            os.makedirs(self.download_dir)
        
        # Set Chrome options and preferences
        chrome_options = webdriver.ChromeOptions()
        chrome_prefs = {
            "download.default_directory": self.download_dir,
            "profile.default_content_settings.popups": 0,
            "download.prompt_for_download": False,
        }
        chrome_options.add_experimental_option("prefs", chrome_prefs)
        
        # Initialize the WebDriver with the options
        self.driver = webdriver.Chrome(options=chrome_options)
        
        # Navigate to your target URL but fail the test if it takes too long
        self.driver.set_page_load_timeout(10)
        self.driver.get("http://localhost:3000")
    
    def test_csv_download(self):
        try:
            csv_testpage = self.driver.find_element(By.XPATH, '//a[@href="/csv_testpage"]')
        except:
            self.fail("Button to csv testpage not found!")
        csv_testpage.click()
        sleep(1)
        #find the button for mass export but throw an appropriate error if it isnt found
        try:
            exportManyButton = self.driver.find_element(By.NAME, "csvMassExportButt")
        except:
            self.fail("Button for mass export not found!")
        exportManyButton.click()
        try:
            alert = self.driver.switch_to.alert
            self.assertTrue(True, "Alert is present!")
            print("Alert was present!")
            alert.accept()
        except NoAlertPresentException:
            self.fail("No error was thrown when exporting 0 athletes")
        
        # Ensure download directory is correctly set
        
        # Test single export button but throw an appropriate error if it isnt found
        try:
            exportSingleButton = self.driver.find_element(By.NAME, "csvSingleExportButt")
        except:
            self.fail("Button for single export not found!")
        exportSingleButton.click()
        butt_id = exportSingleButton.get_attribute("id")
        downloaded_id = self.extract_digits_until_non_digit(butt_id)
        
        # Wait for the file to download
        sleep(1)
        
        # Verify file downloaded to the correct location
        files = os.listdir(self.download_dir)
        self.assertTrue(len(files) > 0, "No file was downloaded!")
        print("File with one athlete was downloaded!")
        exportCheckBoxes = self.driver.find_elements(By.NAME, "csvCheckbox")
        #make sure there are checkboxes to click
        self.assertTrue(len(exportCheckBoxes) > 0, "No checkboxes to click!")
        #test the export many button
        for checkBox in exportCheckBoxes:
            checkBox.click()
        exportManyButton.click()
        
        sleep(1)
        
        files = os.listdir(self.download_dir)
        self.assertTrue(len(files) > 1, "No second file was downloaded!")
        print("File with multiple athletes was downloaded!")
    
    def tearDown(self):
        # Close the browser
        self.driver.quit()
        self.delete_files_in_directory("./test_download_dir")
        print("Test CSV Export Success!")
        

if __name__ == "__main__":
    unittest.main()
    
