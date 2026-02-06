import time

def test_guest_should_see_add_to_cart_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    button_selectors = [
        "button.btn-add-to-basket",  # основной селектор
        ".add-to-basket button",      # альтернативный
        "#add_to_basket_form button", # еще один вариант
        "button[type='submit']"       # общий селектор
    ]
    
    button_found = False
    for selector in button_selectors:
        try:
            button = browser.find_element_by_css_selector(selector)
            if button.is_displayed():
                button_found = True
                print(f"Кнопка найдена с селектором: {selector}")
                break
        except:
            continue
    assert button_found, "Кнопка добавления в корзину не найдена на странице"
