from selenium.webdriver.common.by import By


class navigation_menue:
    URL = 'https://www.amazon.com/'
    open_ele = (By.XPATH, '//i[@class="hm-icon nav-sprite"]')
    Amazon_Music_ele = (By.XPATH, '//a[@class="hmenu-item"]//child::div[text() ="Amazon Music"]')
    Kindle_readers_Books_ele = (By.XPATH, '//div/ul/li/a/div[text() = "Kindle E-readers & Books"]')
    Amazon_Appstore_ele = (By.XPATH, '//div/ul/li/a/div[text() = "Amazon Appstore"]')
    electronics_ele = (By.XPATH, '//div/ul/li/a/div[text() = "Electronics"]')
    Computers_ele = (By.XPATH, '//div/ul/li/a/div[text() = "Computers"]')
    Smart_Home_ele = (By.XPATH, '//a[@class="hmenu-item"]//child::div[text() ="Smart Home"]')
    Arts_Crafts_ele = (By.XPATH, '//a[@class="hmenu-item"]//child::div[text() ="Arts & Crafts"]')
    See_all_ele = (By.XPATH, '//div/ul/li/a/div[text() = "See all"]')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)
        self.browser.implicitly_wait(30)

    def open_menu(self):
        open_element = self.browser.find_element(*self.open_ele)
        self.browser.implicitly_wait(10)
        open_element.click()

    def amazon_music_all(self):
        amazon_music_element = self.browser.find_element(*self.Amazon_Music_ele)
        amazon_music_assert = amazon_music_element.text
        return amazon_music_assert

    def kindle_all(self):
        kindle_readers_Books_element = self.browser.find_element(*self.Kindle_readers_Books_ele)
        kindle_readers_Books_assert = kindle_readers_Books_element.text
        return kindle_readers_Books_assert

    def amazon_appstore_all(self):
        amazon_appstore_element = self.browser.find_element(*self.Amazon_Appstore_ele)
        amazon_appstore_assert = amazon_appstore_element.text
        return amazon_appstore_assert

    def electronics_all(self):
        electronics_element = self.browser.find_element(*self.electronics_ele)
        electronics_assert = electronics_element.text
        return electronics_assert

    def computers_all(self):
        computers_element = self.browser.find_element(*self.Computers_ele)
        computers_assert = computers_element.text
        return computers_assert

    def smart_home_all(self):
       smart_home_element = self.browser.find_element(*self.Smart_Home_ele)
       smart_home_assert = smart_home_element.text
       return smart_home_assert

    def arts_crafts_all(self):
        arts_crafts_element = self.browser.find_element(*self.Arts_Crafts_ele)
        arts_crafts_assert = arts_crafts_element.text
        return arts_crafts_assert

    def see_all(self):
        see_all_element = self.browser.find_element(*self.See_all_ele)
        see_all_assert = see_all_element.text
        return see_all_assert


















