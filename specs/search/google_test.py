import pytest  
from page_objects.google_page import GooglePage
import time

  
# @pytest.mark.search  
# def test_google_search_functionality(chrome_browser):  
#     """  
#     Test the search functionality of google
#     """  
#     url = "https://google.com"  
#     google_page = GooglePage(chrome_browser)  
  
#     google_page.open(url)  
  
#     google_page.search("QA Automation Tools")
#     time.sleep(3)  
#     search_results = google_page.get_search_results()
#     for index, result in enumerate(search_results, 0):
#       print(f"{index}. {result.text}")
  
@pytest.mark.search  
def test_google_news_tab(chrome_browser):  
    """  
    Test the news tab functionality of google
    """  
    url = "https://google.com?hl=en"  
    google_page = GooglePage(chrome_browser)  
  
    google_page.open(url)  
  
    google_page.search("QA Automation Tools")
    time.sleep(3)  
    google_page.click_news_link()
    # time.sleep(3)  

    google_page.get_articles_by_date()

  

