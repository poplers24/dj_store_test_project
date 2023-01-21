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
from pages.profile_page import Profile_page


def test_login_logout():
    driver = webdriver.Chrome("/Users/Maksim/Desktop/Python_auto/resource/chromedriver")

    #Test data

    email = "gofigure844@gmail.com"
    password = "13Zumla4"

    name = "Иван Григорьев"
    number_phone = "8-929-0000010"


    mp = Main_page(driver)
    mp.open_main_page()
    mp.authorization(email, password)

    pp = Profile_page(driver)
    pp.assert_profile_data(name, email, number_phone)
    pp.logout_profile()

    time.sleep(5)
    driver.quit()
    print("Browser close")