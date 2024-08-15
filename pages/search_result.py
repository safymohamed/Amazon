from selenium.webdriver.common.by import By

class search_result_page:
    search_result_ele = (By.XPATH, '//div[@class="a-section a-spacing-small a-spacing-top-small"]')

    def __init__(self, browser):
        self.browser = browser

    def search_result(self):
     result_element = self.browser.find_elements(*self.search_result_ele)
     self.browser.implicitly_wait(10)
     result = [i.text for i in result_element]
     return result






