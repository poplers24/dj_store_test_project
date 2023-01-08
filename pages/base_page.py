
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Base_page(Base):

    url = "https://www.dj-store.ru/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    catalog_button = "//a[@id='catalog-button']"
    category_piano_keys = "//ul[@id='nav-menu']//span[text()='Клавиши']"
    section_synthesizers = "//ul[@id='nav-menu']//a[text()='Синтезаторы']"

    # Getters

    def get_catalog_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog_button)))

    def get_category_piano_keys(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.category_piano_keys)))

    def get_section_synthesizers(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.section_synthesizers)))

    # Actions

    def open_site(self):
        self.driver.get(self.url)
        print("Browser open on the main page")

    def click_catalog_button(self):
        self.get_catalog_button().click()
        print("Click catalog button")

    def cursor_on_category_piano_keys(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_category_piano_keys()).perform()
        print("Cursor hovered over keys")

    def click_on_section_synthesizers(self):
        self.get_section_synthesizers().click()
        print("Click on subsection synthesizers")

    # Method

    def go_to_synth_section(self):
        self.open_site()
        self.get_current_url()
        self.click_catalog_button()
        self.cursor_on_category_piano_keys()
        self.click_on_section_synthesizers()
        self.get_current_url()
        self.assert_url("https://www.dj-store.ru/oborudovanie/klavishi/sintezatory/")





