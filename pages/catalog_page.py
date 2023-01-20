import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilites.logger import Logger


class Catalog_page(Base):

    url = "https://www.dj-store.ru/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    h1_catalog_page = "//h1[@itemprop='name']"
    breadcrumbs_now = "//li[@itemprop='itemListElement']/span[@itemprop='name']"
    slider_arrow_next = "//div[@id='category-slider-next']"
    slider_arrow_back = "//div[@id='category-slider-prev']"
    slider_price_filter_left = "//span[@class='irs-slider from']"
    slider_price_filter_right = "//span[@class='irs-slider to']"
    button_filter = "//button[@class='filter-button']"

    # Getters

    def get_h1_catalog_page(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.h1_catalog_page)))

    def get_breadcrumbs_now(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.breadcrumbs_now)))

    def get_slider_arrow_next(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.slider_arrow_next)))

    def get_slider_arrow_back(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.slider_arrow_back)))

    """Получаем локатор нужной категории в слайдере"""
    def get_slider_category(self, slider_category):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
            f"//ul[@id='cat-items']/li/a/span[text()='{slider_category}']")))

    def get_slider_price_filter_left(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.slider_price_filter_left)))

    def get_slider_price_filter_right(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.slider_price_filter_right)))

    def get_button_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_filter)))

    def get_title_product_in_catalog(self, title_product):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
            f"//div[@id='cat-items']//a[text()='{title_product}']")))

    """Получем локатор нужного производителя в фильтре"""
    def get_brand_in_filter(self, brand):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
            f"//aside[@class='filter-item']/ul/li/a/span[text()='{brand}']")))

    """Получаем локатор цены у нужного товара"""
    def get_price_product_in_catalog(self, product):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
            f"//div[@class='prod_li ']/a[@title='{product}']/following::div[@class='list-right'][1]/"
            f"div[@class='list-right-wrapper']/p[@class='price']/span[1]")))

    """Получаем локатор кнопки добавить В корзину у нужного товара"""
    def get_button_to_cart(self, product):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
            f"//div[@class='prod_li ']/a[@title='{product}']/following::div[@class='list-right'][1]/"
            f"p/a[@class='button cart_but tooltip']")))

    """Получаем локатор кнопки Перейти в корзину у нужного товара"""
    def get_button_go_to_cart(self, product):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
            f"//div[@class='prod_li ']/a[@title='{product}']/following::div[@class='list-right'][1]/"
            f"p/a[@class='button cart_but tooltip']")))

    # Actions

    @allure.step
    def click_slider_arrow_next(self):
        self.get_slider_arrow_next().click()
        print("Click slider arrow next")

    @allure.step
    def click_slider_category(self, slider_category):
        self.get_slider_category(slider_category).click()
        print("Click slider category - " + slider_category)

    @allure.step
    def interaction_left_slider_price(self, x_left):
        action = ActionChains(self.driver)
        action.click_and_hold(self.get_slider_price_filter_left()).move_by_offset(x_left, 0).release().perform()
        print("Slider moved to the right")

    @allure.step
    def interaction_right_slider_price(self, x_right):
        action = ActionChains(self.driver)
        action.click_and_hold(self.get_slider_price_filter_right()).move_by_offset(x_right, 0).release().perform()
        print("Slider moved to the left")

    @allure.step
    def click_button_filter(self):
        self.get_button_filter().click()
        print("Click button filter")

    @allure.step
    def click_title_product_in_catalog(self, title_product):
        self.get_title_product_in_catalog(title_product).click()
        print("Click on title product in catalog")

    @allure.step
    def click_brand_in_filter(self, brand):
        self.get_brand_in_filter(brand).click()
        print("Click on brand in filter - " + brand)

    @allure.step
    def click_button_to_cart(self, product):
        self.get_button_to_cart(product).click()
        print("Click button to cart")

    @allure.step
    def read_price_product(self, product):
        price = self.get_price_product_in_catalog(product).text()
        return price

    @allure.step
    def click_button_go_to_cart(self, product):
        self.get_button_go_to_cart(product).click()
        print("Click button to go cart")

    # Method

    """Переходим в раздел через слайдер"""
    def go_to_next_section_in_slider(self, slider_category):
        with allure.step("Go to next section in slider"):
            Logger.add_start_step(method="go_to_next_section_in_slider")
            self.click_slider_arrow_next()
            self.click_slider_category(slider_category)
            self.get_current_url()
            self.assert_h1(self.get_h1_catalog_page(), slider_category)
            self.assert_breadcrumbs_now(self.get_breadcrumbs_now(), slider_category)
            Logger.add_end_step(url=self.driver.current_url, method="go_to_next_section_in_slider")

    """Настраиваем диапазон цены ползунками и нажимаем кнопку применить"""
    def set_the_price_slider(self, x_left, x_right):
        with allure.step("Set the price slider"):
            Logger.add_start_step(method="set_the_price_slider")
            self.scroll_page(400)
            self.interaction_left_slider_price(x_left)
            self.interaction_right_slider_price(x_right)
            self.click_button_filter()
            self.get_current_url()
            Logger.add_end_step(url=self.driver.current_url, method="set_the_price_slider")

    def go_to_product_page(self, title_product):
        with allure.step("Go to product page"):
            Logger.add_start_step(method="go_to_product_page")
            self.scroll_page(500)
            self.click_title_product_in_catalog(title_product)
            self.get_current_url()
            self.assert_h1(self.get_h1_catalog_page(), title_product)
            self.assert_breadcrumbs_now(self.get_breadcrumbs_now(), title_product)
            Logger.add_end_step(url=self.driver.current_url, method="go_to_product_page")














