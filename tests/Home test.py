from pages.HomePage import Home_page

def test_amazon_Home(browser):
    load_obj = Home_page(browser)
    logo = "Amazon"
    location = "Egypt"
    search = "Search Amazon"
    language = "Choose a language for shopping."
    signin_text = "Hello, sign in"
    Return_text = "Returns"
    All_list_text = 'All'
    today_deals_text = "Today's Deals"
    Customer_text = "Customer Service"
    Registry_text = "Registry"
    Gift_Cards_text = "Gift Cards"
    Sell_text = "Sell"
    department_value = "Toys & Games"
    language_text = "الكل"
    
    load_obj.load()
    assert load_obj.logo_nav() == logo
    assert load_obj.deliver_to_Egypt_nav() == location
    assert load_obj.search_Amazon_nav() == search
    assert load_obj.language_nav() == language
    assert load_obj.sign_in_nav() == signin_text
    assert load_obj.Return_nav() == Return_text
    assert load_obj.All_list_nav() == All_list_text
    assert load_obj.Today_Deals_nav() == today_deals_text
    assert load_obj.Customer_service_nav() == Customer_text
    assert load_obj.Registry_nav() == Registry_text
    assert load_obj.Gift_cards_nav() == Gift_Cards_text
    assert load_obj.Sell_nav() == Sell_text
    assert load_obj.All_department() == department_value
    load_obj.change_language() == language_text







