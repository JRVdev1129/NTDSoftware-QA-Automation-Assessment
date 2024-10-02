"""  
Base Page object 
"""  
  
from selenium.webdriver.common.by import By  
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import dateparser

  
class BasePage:  
    def __init__(self, driver):  
        self.driver = driver
  
    def open(self, url):  
        self.driver.get(url)  
        
    def get_selector(self, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, locator)))
        return element
    
    def get_selectors(self, locator):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, locator)))
        return self.driver.find_elements(By.CSS_SELECTOR, locator)
    
    def get_name(self, text):
        return self.driver.find_element(By.NAME, text)
    
    def get_link_text(self, text):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, text)))
        return element
    
    def parse_date(self, date):
        parsed_date = dateparser.parse(date)
        return parsed_date
  
