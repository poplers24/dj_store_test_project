import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilites.logger import Logger


class Profile_page(Base):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators

    profile_name = "//div[@class='profile-header']/p[@class='name']/span"
    profile_email = "//div[@class='left-col'][1]//p[1]"
    profile_number_phone = "//div[@class='left-col'][1]//p[2]"
    button_logout_profile = "//div[@class='logout personal-area-logout']//span"
    user_block_icon_profile = "//div[@class='header clear']//li[@class='login']//span"

    # Getters

    def get_profile_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.profile_name)))

    def get_profile_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.profile_email)))

    def get_profile_number_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.profile_number_phone)))

    def get_button_logout_profile(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_logout_profile)))

    def get_user_block_icon_profile(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_block_icon_profile)))

    # Actions

    @allure.step
    def should_by_valid_profile_name(self, name):
        value_name = self.get_profile_name().text
        assert value_name == name, "Profile name does not match"
        print("Profile name is correct - " + value_name)

    @allure.step
    def should_by_valid_profile_email(self, email):
        value_email = self.get_profile_email().text
        assert value_email == email, "Profile email does not match"
        print("Profile email is correct - " + value_email)

    @allure.step
    def should_by_valid_profile_number_phone(self, phone_number):
        value_number_phone = self.get_profile_number_phone().text
        assert value_number_phone == phone_number, "Profile email does not match"
        print("Profile number phone is correct - " + value_number_phone)

    @allure.step
    def click_button_logout_profile(self):
        self.get_button_logout_profile().click()
        print("Click button logout profile")
        time.sleep(2)

    @allure.step
    def should_by_user_icon_signature_changed(self):
        signature = self.get_user_block_icon_profile().text
        assert signature == "Войти", "Profile email does not match"
        print("Signature under the user icon changed on - " + signature)

    # Method

    def assert_profile_data(self, name, email, phone_number):
        with allure.step("Assert profile data"):
            Logger.add_start_step(method="assert_profile_data")
            self.should_by_valid_profile_name(name)
            self.should_by_valid_profile_email(email)
            self.should_by_valid_profile_number_phone(phone_number)
            Logger.add_end_step(url=self.driver.current_url, method="assert_profile_data")

    def logout_profile(self):
        with allure.step("Logout profile"):
            Logger.add_start_step(method="logout_profile")
            self.click_button_logout_profile()
            self.should_by_user_icon_signature_changed()
            Logger.add_end_step(url=self.driver.current_url, method="logout_profile")


