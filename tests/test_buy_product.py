import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.main_page import Main_page
from pages.catalog_page import Catalog_page
from pages.product_page import Product_page


def test_select_product():
    driver = webdriver.Chrome("/Users/Maksim/Desktop/Python_auto/resource/chromedriver")

    # Test data
    category_nav_menu = "Клавиши"
    category_on_display_menu = "Синтезаторы"
    slider_category = "Звуковые модули"
    title_product = "Драм-машина Vermona DRM 1 MKIII Trigger Chrom"

    print("\nStart test")

    mp = Main_page(driver)
    mp.go_to_catalog_via_hover_menu(category_nav_menu, category_on_display_menu)

    cp = Catalog_page(driver)
    cp.go_to_next_section_in_slider(slider_category)
    cp.set_the_price_slider(30, -80)
    cp.go_to_product_page(title_product)

    pp = Product_page(driver)
    pp.add_product_to_cart(title_product)



    time.sleep(10)
    driver.quit()
    print("Browser close")