link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"


def test_should_be_add_to_basket_button(browser):
    browser.get(link)
    browser.find_element_by_css_selector(".btn-add-to-basket")