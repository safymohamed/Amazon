from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class search_funcitinuly:
    URL = "https://www.amazon.com/"

    search_element = (By.XPATH, '//div[@class="nav-search-field "]//child::input')

    def __init__(self, browser):
     self.browser = browser

    def load(self):
        self.browser.get(self.URL)
        self.browser.implicitly_wait(30)

    def valied_input_search(self, valid):
      search_ele = self.browser.find_element(*self.search_element)
      self.browser.implicitly_wait(5)
      search_ele.send_keys(valid + Keys.RETURN)

