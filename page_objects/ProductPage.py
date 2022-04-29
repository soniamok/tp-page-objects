from selenium import webdriver
from selenium.webdriver.common.by import By


class ProductPage:
    cart = "input#add-to-cart-button"

    def __init__(self, driver: webdriver):
        self.driver = driver

    def addToCart(self):
        self.driver.find_element(By.CSS_SELECTOR, self.cart).click()


