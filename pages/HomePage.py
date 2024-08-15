
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class Home_page:
    URL = "https://www.amazon.com/"
    logo_ele = (By.ID, 'nav-logo-sprites')
    deliver_ele = (By.ID, 'glow-ingress-line2')
    search_ele = (By.XPATH, '//div[@class="nav-search-field "]//child::input')
    EN_ele = (By.XPATH, '//div[@class="layoutToolbarPadding"]//child::a')
    signin_nav_ele = (By.XPATH, '//div[@class="nav-line-1-container"]//child::span')
    Return_nav_ele = (By.XPATH, '//span[text()="Returns"]')
    All_list_ele = (By.XPATH, '//span[@class="hm-icon-label"]')
    Today_Deals_ele = (By.XPATH, '//div[@class="nav-progressive-content"]//child::a[1]')
    Customer_service_ele = (By.XPATH, '//div[@class="nav-progressive-content"]//child::a[2]')
    Registry_ele = (By.XPATH, '//div[@class="nav-progressive-content"]//child::a[3]')
    Gift_Cards_ele = (By.XPATH, '//div[@class="nav-progressive-content"]//child::a[4]')
    Sell_ele = (By.XPATH, '//div[@class="nav-progressive-content"]//child::a[5]')
    all_department_ele = (By.XPATH, '//select[@class="nav-search-dropdown searchSelect nav-progressive-attrubute nav-progressive-search-dropdown"]')
    choose_department_ele = (By.XPATH, '//select[@class="nav-search-dropdown searchSelect nav-progressive-attrubute nav-progressive-search-dropdown"]//child::option[26]')
    assert_depart_ele = (By.ID, 'nav-search-label-id')
    language_ele = (By.XPATH, '//a[@href="/customer-preferences/edit?ie=UTF8&preferencesReturnUrl=%2F&ref_=topnav_lang_ais"]')
    AR_ele = (By.XPATH, '//div[@id="nav-flyout-icp"] //descendant :: a[@href="#switch-lang=ar_AE"]')
    language_assert_ele = (By.XPATH, '//span[@class="hm-icon-label"]')

    def __init__(self, browser):
     self.browser = browser

    def load(self):
     self.browser.get(self.URL)
     self.browser.implicitly_wait(30)

    def logo_nav(self):
      logo_element = self.browser.find_element(*self.logo_ele)
      logo_assert = logo_element.get_attribute('aria-label')
      return logo_assert

    def deliver_to_Egypt_nav(self):
      deliver_Egypet_element = self.browser.find_element(*self.deliver_ele)
      deliver_Egypet_assert = deliver_Egypet_element.text
      return deliver_Egypet_assert

    def search_Amazon_nav(self):
      search_Amazon_element = self.browser.find_element(*self.search_ele)
      self.browser.implicitly_wait(5)
      search_Amazon_assert = search_Amazon_element.get_attribute('aria-label')
      return search_Amazon_assert

    def language_nav(self):
      EN_element = self.browser.find_element(*self.EN_ele)
      self.browser.implicitly_wait(5)
      EN_assert = EN_element.get_attribute('aria-label')
      return EN_assert

    def sign_in_nav(self):
      signin_nav_element = self.browser.find_element(*self.signin_nav_ele)
      self.browser.implicitly_wait(5)
      signin_nav_assert = signin_nav_element.text
      return signin_nav_assert

    def Return_nav(self):
      Return_nav_element = self.browser.find_element(*self.Return_nav_ele)
      self.browser.implicitly_wait(5)
      Return_nav_assert = Return_nav_element.text
      return Return_nav_assert

    def All_list_nav(self):
      All_list_element= self.browser.find_element(*self.All_list_ele)
      self.browser.implicitly_wait(5)
      All_list = All_list_element.text
      return All_list

    def Today_Deals_nav(self):
      today_Deals_element = self.browser.find_element(*self.Today_Deals_ele)
      self.browser.implicitly_wait(5)
      today_Deals= today_Deals_element.text
      return today_Deals

    def Customer_service_nav(self):
      Customer_element = self.browser.find_element(*self.Customer_service_ele)
      self.browser.implicitly_wait(5)
      customer = Customer_element.text
      return customer

    def Registry_nav(self):
      Registry_element = self.browser.find_element(*self.Registry_ele)
      self.browser.implicitly_wait(5)
      Registry= Registry_element.text
      return Registry

    def Gift_cards_nav(self):
      Gift_element = self.browser.find_element(*self.Gift_Cards_ele)
      self.browser.implicitly_wait(5)
      Gift_cards = Gift_element.text
      return Gift_cards

    def Sell_nav(self):
      Sell_element = self.browser.find_element(*self.Sell_ele)
      self.browser.implicitly_wait(5)
      Sell = Sell_element.text
      return Sell

    def All_department(self):
       all_department_element = self.browser.find_element(*self.all_department_ele)
       self.browser.implicitly_wait(5)
       all_department_element.click()
       choose_department_element=self.browser.find_element(*self.choose_department_ele)
       self.browser.implicitly_wait(5)
       choose_department_element.click()
       department_element = self.browser.find_element(*self.assert_depart_ele)
       self.browser.implicitly_wait(5)
       assert_department = department_element.text
       return assert_department

    def change_language(self):
      language_element = self.browser.find_element(*self.language_ele)
      self.browser.implicitly_wait(20)
      chain = ActionChains(self.browser)
      chain.move_to_element(language_element).perform()
      self.browser.implicitly_wait(40)
      AR_element = self.browser.find_element(*self.AR_ele)
      self.browser.implicitly_wait(20)
      AR_element.click()
      # language_assert_element = self.browser.find_element(*self.language_assert_ele)
      # language_assert = language_assert_element.text
      # return language_assert

    



