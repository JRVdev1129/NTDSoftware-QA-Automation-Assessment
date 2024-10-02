import pytest  
from selenium import webdriver  
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService  
from webdriver_manager.chrome import ChromeDriverManager  
  
  
@pytest.fixture()  
def chrome_browser():  
    options = Options()
    options.add_argument("--lang=en")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # driver = webdriver.Chrome(options=options)  
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)  

    driver.delete_all_cookies()
  
      
    driver.implicitly_wait(10)  
    # Yield the WebDriver instance  
    yield driver  
    # Close the WebDriver instance  
    driver.quit()
