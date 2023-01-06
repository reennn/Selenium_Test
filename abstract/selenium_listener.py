from selenium.webdriver.support.events import AbstractEventListener

from base.selenium_base import SeleniumBase


class MyListener(AbstractEventListener):

    # метод удаления куки до клика на ссылку
    def before_click(self, element, driver):
        SeleniumBase(driver).delete_cookie('ak_bmsc')

    # метод удаления куки после клика на ссылку
    def after_click(self, element, driver):
        SeleniumBase(driver).delete_cookie('ak_bmsc')
