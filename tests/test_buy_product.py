import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import Base_page

def test_select_product():
    driver = webdriver.Chrome("/Users/Maksim/Desktop/Python_auto/resource/chromedriver")

    print("\nStart test")

    mp = Base_page(driver)
    mp.go_to_synth_section()


    time.sleep(5)
    driver.quit()
    print("Browser close")