from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  
from selenium.common.exceptions import NoSuchElementException
import time


  
class GooglePage(BasePage):
    def __init__(self, driver):
      super().__init__(driver) 
  
    def search_bar(self):  
        return self.getSelector('textarea[name="q"]')
        
  
    def search(self, query):  
        search_box = self.search_bar()
        search_box.send_keys(query + Keys.RETURN) 
    
    def get_search_results(self):
        view_mote_button = self.getSelector('#Odp5De  div[role="button"]  span > span:first-child')
        view_mote_button.click()
        
        results = self.getSelectors("div.sinMW")
        filtered_results = [result for result in results if result.text.strip()]
        return filtered_results[:11]

  