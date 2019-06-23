'''
запускать
pytest --language="es" test_items.py
pytest --language="fr" test_items.py

language="fr" должна быть фраза на кнопке добавления в корзину: "Ajouter au panier"
'''
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
btn_class = 'btn-add-to-basket'


def test_guest_should_see_basket_button(browser):
    browser.get(link)
    button = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, btn_class))
    )
    time.sleep(30)
