from pages.search import search_funcitinuly
from pages.search_result import search_result_page


def test_amazon_search(browser):

 search_obj = search_funcitinuly(browser)
 search_result_obj = search_result_page(browser)
 valid = "i phone"

 search_obj.load()
 search_obj.valied_input_search(valid)
 titles = search_result_obj.search_result()
 matches = [t for t in titles if valid.lower() in t.lower()]
 assert len(matches) > 0

