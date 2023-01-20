import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilites.logger import Logger


class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators

    h1_product_page = "//h1[@itemprop='name']"
    product_in_cart_items = "//table//a"
    price_product_in_cart_items = "//div[@class='cart-order-price-count']"
    total_to_pay = "//div[@id='total_to_pay']"
    input_email = "//input[@name='email']"
    button_go_to_shipping_method = "//button[@id='next_step_of_placing_an_order']"
    input_fio = "//input[@id='fio']"
    input_phone = "//input[@id='phone']"
    button_pickup = "//span[@class='delivery-second']"
    radiobutton_pickup_msk = "//label[@for='delivery_mode_shop_msk']"
    button_go_to_payment_method = "//button[@id='next_step_of_placing_an_order']"
    select_payment_mode = "//select[@id='payment_mode']"



    # Getters

    def get_h1_catalog_page(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.h1_product_page)))

    def get_product_in_cart_items(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_in_cart_items)))

    def get_price_product_in_cart_items(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_product_in_cart_items)))

    def get_total_to_pay(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.total_to_pay)))

    def get_input_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_email)))

    def get_button_go_to_shipping_method(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_go_to_shipping_method)))

    def get_input_fio(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_fio)))

    def get_input_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_phone)))

    def get_button_pickup(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_pickup)))

    def get_radiobutton_pickup_msk(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.radiobutton_pickup_msk)))

    def get_button_go_to_payment_method(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_go_to_payment_method)))

    def get_select_payment_mode(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_payment_mode)))

    # Actions

    @allure.step
    def assert_product_in_cart_items(self, title_product):
        product_cart_item = self.get_product_in_cart_items().text
        assert product_cart_item in title_product, "Items in the cart do not match"
        print("Items in cart match")

    @allure.step
    def assert_price_product_in_cart_items(self, price_product):
        price_product_in_item_cart = self.get_price_product_in_cart_items().text
        assert price_product in price_product_in_item_cart, "Price product not match price product in cart items"
        print("Price product in cart match")

    @allure.step
    def assert_total_to_pay(self, sum_price_product):
        total_order_cart = self.get_total_to_pay().text
        assert sum_price_product in total_order_cart, "Order amount is not correct"
        print("Order amount is correct")

    @allure.step
    def input_user_email(self, email):
        self.get_input_email().send_keys(email)
        print("Input user email")

    @allure.step
    def click_button_go_to_shipping_method(self):
        self.get_button_go_to_shipping_method().click()
        print("Click button go to shipping method")

    @allure.step
    def input_user_fio(self, fio):
        self.get_input_fio().send_keys(fio)
        print("Input user fio")

    @allure.step
    def input_user_phone(self, phone):
        self.get_input_phone().send_keys(phone)
        print("Input user phone")

    @allure.step
    def click_button_pickup(self):
        self.get_button_pickup().click()
        print("Click button pickup")

    @allure.step
    def click_radiobutton_pickup_msk(self):
        self.get_radiobutton_pickup_msk().click()
        print("Click radiobutton pickup msk")

    @allure.step
    def click_button_go_to_payment_method(self):
        self.get_button_go_to_payment_method().click()
        print("Click button go to payment method")

    @allure.step
    def payment_select_cash(self):
        select = Select(self.get_select_payment_mode())
        select.select_by_index(1)
        print("Select payment cash")



    # Method

    def check_product_in_cart(self, title_product, price_product):
        with allure.step("Check product in cart"):
            Logger.add_start_step(method="check_product_in_cart")
            self.assert_product_in_cart_items(title_product)
            self.assert_price_product_in_cart_items(price_product)
            self.assert_total_to_pay(price_product)
            Logger.add_end_step(url=self.driver.current_url, method="check_product_in_cart")

    def ordering(self, email, fio, phone):
        with allure.step("Ordering"):
            Logger.add_start_step(method="ordering")
            self.input_user_email(email)
            self.click_button_go_to_shipping_method()
            self.input_user_fio(fio)
            self.input_user_phone(phone)
            self.click_button_pickup()
            self.click_radiobutton_pickup_msk()
            self.click_button_go_to_payment_method()
            self.payment_select_cash()
            Logger.add_end_step(url=self.driver.current_url, method="ordering")





