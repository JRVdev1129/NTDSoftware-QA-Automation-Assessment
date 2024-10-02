"""  
Base Page object 
"""  
  
from selenium.webdriver.common.by import By  
  
  
class BasePage:  
    def __init__(self, driver):  
        self.driver = driver
  
    def open(self, url):  
        self.driver.get(url)  
        
    def getSelector(self, locator):
        return self.driver.find_element(By.CSS_SELECTOR, locator)
    
    def getSelectors(self, locator):
        return self.driver.find_elements(By.CSS_SELECTOR, locator)
    
    def getName(self, locator):
        return self.driver.find_element(By.NAME, locator)
  
