import datetime
import time

from selenium.webdriver import ActionChains


class Base():
    def __init__(self, driver):
        self.driver = driver

    """Method get current url"""

    def get_current_url(self):
        time.sleep(1)
        get_url = self.driver.current_url
        print("Current url " + get_url)

    """Method Screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime("%H.%M.%S.%Y.%m.%d")
        name_screenshot = 'screenshot_' + now_date + '.png'
        self.driver.save_screenshot(
            '/Users/Maksim/Desktop/Python_auto/dj_store_test_project/screen/' + name_screenshot)

    """Method assert url"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert result in get_url, "Value url does not match the expected result"
        print("Good value url")

    """Method assert h1 page"""

    def assert_h1(self, h1, result):
        value_h1 = h1.text
        assert result in value_h1, "Value h1 does not match the expected result"
        print("Good value h1 page - " + value_h1)

    """Method assert breadcrumbs now page"""

    def assert_breadcrumbs_now(self, breadcrumbs_now, result):
        value_breadcrumbs_now = breadcrumbs_now.text
        assert value_breadcrumbs_now in result, "Value breadcrumbs now does not match the expected result"
        print("Good value breadcrumbs now page - " + value_breadcrumbs_now)

    """Method scroll to element"""

    def scroll_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    """Method scroll page"""

    def scroll_page(self, value):
        self.driver.execute_script(f"window.scrollTo(0, {value})")

    """Method assert that the product has been added to the cart"""

    def assert_title_product_in_window_cart(self, title_product, title_in_window_cart):
        title_product_in_window_cart = title_in_window_cart.text
        assert title_product_in_window_cart in title_product, "Title product in cart does not match"
        print("Title product in the cart matches - " + title_product_in_window_cart)

    def assert_price_in_window_cart(self, price_product, price_in_window_cart):
        price_product_in_window_cart = price_in_window_cart.text
        assert price_product in price_product_in_window_cart, "The price in the cart window does not match"
        print("Price in window cart - " + price_product_in_window_cart)

    # def assert_price_product_and_total_sum_in_window_cart(self, ):


