from base.selenium_base import SeleniumBase
from base.utils import Utils
from selenium.webdriver.remote.webelement import WebElement
from typing import List


class HomepageNav(SeleniumBase):

    # инициализация необходимых переменных
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__nav_links: str = '#mainNavigationFobs>li'  # то. что необходимо найти
        self.NAV_LINK_TEXT = 'Women, Men, Kids, Home, Beauty, Shoes, Handbags, Jewelry, Furniture, Toys, Gifts, Trending, Sale'
        # выше дана верная строка для сравнения с результатом

    # метод получения видимых элементов
    def get_nav_links(self) -> List[WebElement]:
        return self.are_visible('css', self.__nav_links, 'Header Navigation Links')

    # метод перевода результатов поиска в текстовый вид
    def get_nav_links_text(self) -> str:
        nav_links = self.get_nav_links()  # lıst links
        nav_links_text = self.get_text_from_webelements(nav_links)
        return Utils.join_strings(nav_links_text)

    def get_nav_link_by_name(self, name) -> WebElement:
        elements = self.get_nav_links()
        self.get_element_by_text(elements, name)