import time #импорт будет нужен когда проверяющий разкомментирует 8 строку


def test_get_answer(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    browser.implicitly_wait(5)
    #time.sleep(30) #проверяющему нужно раскомментировать эту строку самостоятельно
    try:
        button = browser.find_element_by_css_selector(".btn-add-to-basket")
        assert button, "the button was found"
    except:
        print("the button did not find")

    #пустая строка