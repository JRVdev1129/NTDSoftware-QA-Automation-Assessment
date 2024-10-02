from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def before_all(context):
    # Optional: Set Chrome options for headless mode (uncomment if needed)
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Uncomment to enable headless mode
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1200")
    chrome_options .add_argument("--lang=en")
    chrome_options .add_argument("--no-sandbox")
    chrome_options .add_argument("--disable-dev-shm-usage")
    
    # Use WebDriver Manager to automatically handle driver versioning
    service = Service(ChromeDriverManager().install())
    
    # Initialize the browser and attach it to context
    context.browser = webdriver.Chrome(service=service, options=chrome_options)

def after_all(context):
    # Quit the browser after all tests
    context.browser.quit()
