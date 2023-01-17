
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
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

    # Actions

    def open_site(self):
        self.driver.get(self.url)
        print("Browser open on the main page")

    def click_catalog_button(self):
        self.get_catalog_button().click()
        print("Click catalog button")

    def cursor_on_category_nav_menu(self, category_nav_menu):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_category_nav_menu(category_nav_menu)).perform()
        print("Cursor on nav menu category - " + category_nav_menu)

    def click_on_category_on_display_menu(self, category_on_display_menu):
        self.get_category_on_display_menu(category_on_display_menu).click()
        print("Click on category in display menu - " + category_on_display_menu)

    # Method

    def go_to_catalog_via_hover_menu(self, category_nav_menu, category_on_display_menu):
        Logger.add_start_step(method="go_to_catalog_via_hover_menu")
        self.open_site()
        self.get_current_url()
        self.click_catalog_button()
        self.cursor_on_category_nav_menu(category_nav_menu)
        self.click_on_category_on_display_menu(category_on_display_menu)
        self.get_current_url()
        self.assert_h1(self.get_h1_catalog_page(), category_on_display_menu)
        self.assert_breadcrumbs_now(self.get_breadcrumbs_now(), category_on_display_menu)
        Logger.add_end_step(url=self.driver.current_url, method="go_to_catalog_via_hover_menu")










