from pages.navigation import navigation_menue

def test_amazon_search(browser):
    navigation_obj = navigation_menue(browser)
    amazon_music = "Amazon Music"
    kindle_text = "Kindle E-readers & Books"
    amazon_appstore_text = "Amazon Appstore"
    electronics_text = "Electronics"
    computers_text = "Computers"
    smart_home_text = "Smart Home"
    arts_crafts_text = "Arts & Crafts"
    see_all_text = "See all"

    navigation_obj.load()
    navigation_obj.open_menu()
    assert navigation_obj.amazon_music_all() == amazon_music
    assert navigation_obj.kindle_all() == kindle_text
    assert navigation_obj.amazon_appstore_all() == amazon_appstore_text
    assert navigation_obj.electronics_all() == electronics_text
    assert navigation_obj.computers_all() == computers_text
    assert navigation_obj.smart_home_all() == smart_home_text
    assert navigation_obj.arts_crafts_all() == arts_crafts_text
    assert navigation_obj.see_all() == see_all_text















