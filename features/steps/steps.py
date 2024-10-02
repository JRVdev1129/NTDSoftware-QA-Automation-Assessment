from behave import given, when, then
from page_objects.google_page import GooglePage
import time
url = "https://google.com?hl=en"  

@given('User opens the Google homepage')
def step_open_google_homepage(context):
    context.google_page = GooglePage(context.browser)
    context.google_page.open(url)

@when('User search for "{query}"')
def step_search_google(context, query):
    context.google_page.search(query)
    time.sleep(3)

@then('User should see search results')
def step_verify_search_results(context):
    search_results = context.google_page.get_search_results()
    for index, result in enumerate(search_results, 0):
        print(f"{index}. {result.text}")
    assert len(search_results) > 0, "No search results found!"

@when('User click the News tab')
def step_click_news_tab(context):
    context.google_page.click_news_link()
    time.sleep(3)

@then('User should see news articles')
def step_verify_news_articles(context):
    articles = context.google_page.get_articles_by_date()
    assert len(articles) > 0, "No news articles found!"
