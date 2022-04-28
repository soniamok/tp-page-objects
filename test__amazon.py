from time import sleep
from selenium import webdriver
from page_objects.HomePage import HomePage


def test__amazon1():
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.fr/")
    driver.maximize_window()
    driver.quit()


def test__page__object():
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.fr/")
    homePage = HomePage(driver)
    homePage.closeCookiesPopup()
    homePage.openAllMenu()
    homePage.openBookCategory()
    homePage.openAllBooks()
    driver.quit()
