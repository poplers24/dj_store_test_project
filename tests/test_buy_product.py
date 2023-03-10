import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from pages.cart_page import Cart_page
from pages.main_page import Main_page
from pages.catalog_page import Catalog_page
from pages.product_page import Product_page

@allure.description("Test select product")
def test_select_product():
    driver = webdriver.Chrome("/Users/Maksim/Desktop/Python_auto/resource/chromedriver")

    # Test data
    """product data"""
    category_nav_menu = "Клавиши"
    category_on_display_menu = "Синтезаторы"
    slider_category = "Звуковые модули"
    title_product = "Драм-машина Vermona DRM 1 MKIII Trigger Chrom"
    price_product = "124 571"

    """contact details"""
    email = "extro@pp.com"
    fio = "Сергей Иванов"
    phone = "9992349900"

    print("\nStart test")

    """We open the site on the man page and go to the directoru"""
    mp = Main_page(driver)
    mp.open_main_page()
    mp.go_to_catalog_via_hover_menu(category_nav_menu, category_on_display_menu)

    """Go to the right product"""
    cp = Catalog_page(driver)
    cp.go_to_next_section_in_slider(slider_category)
    cp.set_the_price_slider(30, -80)
    cp.go_to_product_page(title_product)

    """Add tem to cart and go to cart"""
    pp = Product_page(driver)
    pp.add_product_to_cart(title_product, price_product)
    pp.go_to_cart_from_window_cart()

    """We check that the goods in the basket correspond 
    to the added one and place an order"""
    cp = Cart_page(driver)
    cp.check_product_in_cart(title_product, price_product)
    cp.ordering(email, fio, phone)

    time.sleep(5)
    driver.quit()
    print("Browser close")