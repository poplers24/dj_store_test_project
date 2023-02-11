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

@allure.description("Test sregion change")
def test_region_change():
    """Изменение региона"""
    driver = webdriver.Chrome("/Users/Maksim/Desktop/Python_auto/resource/chromedriver")

    #Test data

    city = "Москва"

    print("\nStart test")

    """We open the site on the man page"""
    mp = Main_page(driver)
    mp.open_main_page()

    """Changing the region"""
    mp.region_selection(city)

    time.sleep(5)
    driver.quit()
    print("Browser close")