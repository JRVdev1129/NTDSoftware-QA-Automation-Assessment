# import pytest # uncomment if you want to debug with pytest
from pytest_bdd import scenarios, given, when, then
from page_objects.google_page import GooglePage

url = "https://google.com?hl=en"  
scenarios('google_search.feature')


@given('User opens the Google homepage')
def open_google_homepage(chrome_browser):
    google_page = GooglePage(chrome_browser)
    google_page.open(url)
    
@when('User search for "QA Automation Tools"')
def search_for_qa_automation_tools(chrome_browser):
    google_page = GooglePage(chrome_browser)
    google_page.search("QA Automation Tools")

@then('User should see search results')
def verify_search_results(chrome_browser):
    google_page = GooglePage(chrome_browser)
    search_results = google_page.get_search_results()
    for index, result in enumerate(search_results, 0):
      print(f"{index}. {result.text}")    
    assert len(search_results) >= 10

@when('User clicks the News tab')
def click_news_tab(chrome_browser):
    google_page = GooglePage(chrome_browser)
    google_page.click_news_link()

@then('User should see news articles')
def verify_news_results(chrome_browser):
    google_page = GooglePage(chrome_browser)
    articles = google_page.get_articles_by_date()
    assert len(articles) > 0

# uncomment if you want to debug with pytest
# @pytest.mark.search  
# def test_google_search_functionality(chrome_browser):  
    # """  
    # Test the search functionality of google
    # """  
    # google_page = GooglePage(chrome_browser)  
  
    # google_page.open(url)  
  
    # google_page.search("QA Automation Tools")
    # time.sleep(3)  
    # search_results = google_page.get_search_results()
    # for index, result in enumerate(search_results, 0):
    #   print(f"{index}. {result.text}")
  
# @pytest.mark.search  
# def test_google_news_tab(chrome_browser):  
#     """  
#     Test the news tab functionality of google
#     """  
#     google_page = GooglePage(chrome_browser)  
  
#     google_page.open(url)  
  
#     google_page.search("QA Automation Tools")
#     time.sleep(3)  
#     google_page.click_news_link()
#     # time.sleep(3)  

#     google_page.get_articles_by_date()

  

