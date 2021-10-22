from Navigation_test import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time


def verify_shop_details():
    more_link = driver.find_element(By.XPATH, "//span[@class='font-primary']")
    more_link.click()
    print("More link is active")
    more_page_link = driver.find_element(By.XPATH, "//a[normalize-space()='Shop']")
    more_page_link.click()
    WebDriverWait(driver, 20).until(ec.presence_of_element_located(
        (By.XPATH, "//h2[contains(text(),'Blavity is a tech company for forward thinking Bla')]")))

environment()
page_load()
post_page_load_pop_up()