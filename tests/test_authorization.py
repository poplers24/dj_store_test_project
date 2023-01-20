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

def test_authorization():
    driver = webdriver.Chrome("/Users/Maksim/Desktop/Python_auto/resource/chromedriver")

    #Test data

    email = "gofigure844@gmail.com"
    password = "13Zumla4"


    mp = Main_page(driver)
    mp.open_main_page()
    mp.authorization(email, password)