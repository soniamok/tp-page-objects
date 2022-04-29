from selenium import webdriver
from page_objects.HomePage import HomePage
from page_objects.BooksPage import BooksPage
from page_objects.ProductPage import ProductPage
from page_objects.ConfirmationPage import ConfirmationPage
from page_objects.CartPage import CartPage

def test__amazon1():
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.fr/")
    driver.maximize_window()
    driver.quit()


def test__page__object():
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.fr/")
    target_qty = "2"
    homePage = HomePage(driver)
    homePage.closeCookiesPopup()
    homePage.openAllMenu()
    homePage.openBookCategory()
    homePage.openAllBooks()
    booksPage = BooksPage(driver)
    booksPage.selectFirstBookNouveautes()
    productPage = ProductPage(driver)
    productPage.addToCart()
    confirmationPage = ConfirmationPage(driver)
    confirmationPage.openCart()
    cartPage = CartPage(driver)
    cartPage.changeQuantity("2")
    assert cartPage.getQuantity() == target_qty
    driver.quit()
