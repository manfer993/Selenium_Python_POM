from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def chrome_driver_connection():
    options = Options()
    # options.add_argument("--headless") # Runs Chrome in headless mode.
    options.add_argument('--no-sandbox')  # # Bypass OS security model
    options.add_argument('disable-infobars')
    options.add_argument("--disable-extensions")
    options.add_argument('--disable-gpu')
    # options.add_argument('--window-size=1920,1080')
    options.add_argument('--start-maximized')
    # options.add_argument('incognito')
    # options.add_argument("--verbose")
    return webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def implicitly_wait(self, duration: int):
        self.driver.implicitly_wait(duration)

    def get_url(self):
        return self.driver.current_url

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def get_text(self, *locator):
        return self.driver.find_element(*locator).text

    def get_texts(self, *locator):
        return self.driver.find_elements(*locator).text

    def send_text(self, input_text, *locator):
        self.driver.find_element(*locator).send_keys(input_text)

    def clear_text(self, *locator):
        self.driver.find_element(*locator).clear()

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()
