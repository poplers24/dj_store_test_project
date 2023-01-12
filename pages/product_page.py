import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Product_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators

    h1_product_page = "//h1[@itemprop='name']"
    breadcrumbs_now = "//li[@itemprop='itemListElement']/span[@itemprop='name']"
    button_add_to_cart = "//a[@class='button tooltip cart_but']"
    price_product = "//div[@class='price']//strong"
    button_cart = "//div[@class='header clear']//a[@class='cart-button']"
    window_cart_title_product = "//tr[@class='cart_item']//a"
    window_cart_price_product = "//tr[@class='cart_item']/td[@class='ta-c cart-order-price  cart-order-price-count']"
    window_cart_order_sum = "//div[@class='cart-itogo']//div[@class='cart-order-summa']"
    # Getters

    def get_h1_catalog_page(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.h1_product_page)))

    def get_button_add_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_add_to_cart)))

    def get_price_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_product)))

    def get_button_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_cart)))

    def get_window_cart_title_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.window_cart_title_product)))

    def get_window_cart_price_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.window_cart_price_product)))

    def get_window_cart_order_sum(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.window_cart_order_sum)))

    # Actions

    def click_button_add_to_cart(self):
        self.get_button_add_to_cart().click()
        print("Click button Add to cart")


    def cursor_on_button_cart(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_button_cart()).perform()
        print("Cursor on button cart")

    # Method

    def add_product_to_cart(self, title_product):
        self.click_button_add_to_cart()
        self.cursor_on_button_cart()
        self.assert_title_product_in_window_cart(title_product, self.get_window_cart_title_product())
        self.assert_price_in_window_cart(self.get_price_product(), self.get_window_cart_price_product())