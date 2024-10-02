from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime, timedelta


  
class GooglePage(BasePage):
    def __init__(self, driver):
      super().__init__(driver)
    
    def search_bar(self):  
        return self.getSelector('textarea[name="q"]') 
  
    def view_more_button(self):  
        return self.getSelector('#Odp5De  div[role="button"]  span > span:first-child')
    
    def news_link(self):
        return self.getLinkText("News")
    
    def news_articles(self):
        return self.getSelectors("#rso > div > div > div")
        
  
    def search(self, query):  
        search_box = self.search_bar()
        search_box.send_keys(query + Keys.RETURN) 
    
    def get_search_results(self):
        self.view_more_button().click()
        
        results = self.getSelectors("div.sinMW")
        filtered_results = [result for result in results if result.text.strip()]
        return filtered_results[:11]
    
    def click_news_link(self):
        self.news_link().click()
        
    def get_articles_by_date(self):
        for article in self.news_articles():
            title = article.find_element(By.CSS_SELECTOR,'div[role="heading"]').text
        
            date_text = article.find_element(By.CSS_SELECTOR, 'div span:nth-child(1)').text
            date = self.parse_date(date_text)
            three_months_ago = datetime.now() - timedelta(days=90)

            if date >= three_months_ago:
              print(f"Title: {title}, Date: {date_text}")

  
  