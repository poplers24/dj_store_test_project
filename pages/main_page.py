import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from pages.catalog_page import Catalog_page
from utilites.logger import Logger


class Main_page(Base):

    url = "https://www.dj-store.ru/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    catalog_button = "//a[@id='catalog-button']"
    h1_catalog_page = "//h1[@itemprop='name']"
    breadcrumbs_now = "//li[@itemprop='itemListElement']/span[@itemprop='name']"

    user_block_icon_authorization = "//div[@class='header clear']/div[@class='user-block']/ul/li/a[@href='/profile/login/']"
    input_email = "//div[@id='auth-box']//input[@id='auth_l']"
    input_password = "//div[@id='auth-box']//input[@id='auth_p']"
    button_login = "//div[@id='auth-box']//button"
    user_block_icon_profile = "//div[@class='header clear']/div[@class='user-block']/ul[@id='logged-block-ul']//span[1]"
    city_name_topmenu = "//aside[@class='main-menu hide_in_the_basket_section']/ul/li/a[@id='city_name_topmenu']"
    input_city_choose = "//input[@id='city_chooser_top']"


    # Getters

    def get_catalog_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog_button)))

    """Получаем нужный локатор раздела в выпадающем меню каталога"""
    def get_category_nav_menu(self, category_nav_menu):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
             f"//ul[@id='nav-menu']//span[text()='{category_nav_menu}']")))

    """Получаем нужный локатор подраздела в hover-меню при наведении курсора на раздел в выпадающем меню"""
    def get_category_on_display_menu(self, category_on_display_menu):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
             f"//ul[@id='nav-menu']//a[text()='{category_on_display_menu}']")))

    def get_h1_catalog_page(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.h1_catalog_page)))

    def get_breadcrumbs_now(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.breadcrumbs_now)))

    def get_user_block_icon_authorization(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_block_icon_authorization)))

    def get_input_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_email)))

    def get_input_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_password)))

    def get_button_login(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_login)))

    def get_user_block_icon_profile(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_block_icon_profile)))

    def get_city_name_topmenu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city_name_topmenu)))

    def get_input_city_choose(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_city_choose)))


    # Actions

    @allure.step
    def open_site(self):
        self.driver.get(self.url)
        print("Browser open on the main page")

    @allure.step
    def click_catalog_button(self):
        self.get_catalog_button().click()
        print("Click catalog button")

    @allure.step
    def cursor_on_category_nav_menu(self, category_nav_menu):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_category_nav_menu(category_nav_menu)).perform()
        print("Cursor on nav menu category - " + category_nav_menu)

    @allure.step
    def click_on_category_on_display_menu(self, category_on_display_menu):
        self.get_category_on_display_menu(category_on_display_menu).click()
        print("Click on category in display menu - " + category_on_display_menu)

    @allure.step
    def click_user_block_icon_authorization(self):
        self.get_user_block_icon_authorization().click()
        print("Click icon authorisation")

    @allure.step
    def input_user_email(self, email):
        self.get_input_email().send_keys(email)
        print("Input user email")

    @allure.step
    def input_user_password(self, password):
        self.get_input_password().send_keys(password)
        print("Input user password")

    @allure.step
    def click_button_login(self):
        self.get_button_login().click()
        print("Click button login")

    @allure.step
    def should_by_user_icon_signature_changed(self):
        signature = self.get_user_block_icon_profile().text
        assert signature == "Мой профиль", "Signature under the user icon has not changed"
        print("Signature under the user icon changed on - " + signature)

    @allure.step
    def click_city_name_topmenu(self):
        self.get_city_name_topmenu().click()
        print("Click button city topmenu")

    @allure.step
    def input_choose_city(self, city):
        self.get_input_city_choose().send_keys(city)
        time.sleep(1)
        self.get_input_city_choose().send_keys(Keys.DOWN)
        self.get_input_city_choose().send_keys(Keys.RETURN)
        print("Enter and select a city")

    @allure.step
    def should_by_city_name_in_topmenu(self, city):
        time.sleep(1)
        city_name = self.get_city_name_topmenu().text
        assert city_name == city, f"The selected city {city_name} does not match the expected {city}"
        print(f"The location is displayed correct - {city_name}")

    # Method

    """Open the site on main page"""
    def open_main_page(self):
        with allure.step("Open main page"):
            Logger.add_start_step(method="open_main_page")
            self.open_site()
            self.get_current_url()
            Logger.add_end_step(url=self.driver.current_url, method="open_main_page")

    """Go to the catalog by the menu that opens by clicking the catalog button"""
    def go_to_catalog_via_hover_menu(self, category_nav_menu, category_on_display_menu):
        with allure.step("Go to catalog via hover men"):
            Logger.add_start_step(method="go_to_catalog_via_hover_menu")
            self.click_catalog_button()
            self.cursor_on_category_nav_menu(category_nav_menu)
            self.click_on_category_on_display_menu(category_on_display_menu)
            self.get_current_url()
            self.assert_h1(self.get_h1_catalog_page(), category_on_display_menu)
            self.assert_breadcrumbs_now(self.get_breadcrumbs_now(), category_on_display_menu)
            Logger.add_end_step(url=self.driver.current_url, method="go_to_catalog_via_hover_menu")

    """Open the authorization window and enter the login and password"""
    def authorization(self, email, password):
        with allure.step("Authorization"):
            Logger.add_start_step(method="authorization")
            self.click_user_block_icon_authorization()
            self.input_user_email(email)
            self.input_user_password(password)
            self.click_button_login()
            self.get_current_url()
            self.assert_url("profile")
            self.should_by_user_icon_signature_changed()
            Logger.add_end_step(url=self.driver.current_url, method="authorization")

    """Open the window for changing the region and select another region"""
    def region_selection(self, city):
        with allure.step("Region selection"):
            Logger.add_start_step(method="region_selection")
            self.click_city_name_topmenu()
            self.input_choose_city(city)
            self.should_by_city_name_in_topmenu(city)
            Logger.add_end_step(url=self.driver.current_url, method="region_selection")















