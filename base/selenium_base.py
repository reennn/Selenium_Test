from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from typing import List


class SeleniumBase:

    def __init__(self, driver):
        self.driver = driver
        self.__wait = WebDriverWait(driver, 10, 0.3)  # ожидание для тестирования
        # Используется для  прогрузки всех элементов на странице

    @staticmethod # хз. почему так, но работает
    def __get_selenium_by(find_by: str) -> dict:  # private method __etc. protected _etc.
        find_by = find_by.lower()  # переводим locator в нижний регистр
        locating = {
            'css': By.CSS_SELECTOR,
            'id': By.ID,
            'xpath': By.XPATH,
            'class_name': By.CLASS_NAME,
            'link_text': By.LINK_TEXT,
            'partial_link_text': By.PARTIAL_LINK_TEXT,
            'tag_name': By.TAG_NAME,
            'name': By.NAME,
        }
        # выше заполнен словарь locator'ов
        return locating[find_by]

    # метод для определения видимости элемента
    def is_visible(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(ec.visibility_of_element_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    # метод для определения нахождения элемента (есть/нет)
    def is_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(ec.presence_of_element_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    # метод для определения нахождения элемента (есть/нет)
    def is_not_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(ec.invisibility_of_element_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    # метод для определения видимости элементов!
    def are_visible(self, find_by: str, locator: str, locator_name: str = None) -> List[WebElement]:
        return self.__wait.until(ec.visibility_of_all_elements_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    # метод для определения нахождения элементов (есть/нет)
    def are_present(self, find_by: str, locator: str, locator_name: str = None) -> List[WebElement]:
        return self.__wait.until(ec.presence_of_all_elements_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    # метод получения текста из веб-элементов
    def get_text_from_webelements(self, elements: List[WebElement]) -> List[str]:
        return [element.text for element in elements]  # list comprehension

    # метод нахождения элемента (из списка) по имени
    def get_element_by_text(self, elements: List[WebElement], name: str) -> WebElement:
        name = name.lower()
        return [element for element in elements if element.text.lower() == name][0]

    # метод удаления определенного куки
    def delete_cookie(self, cookie_name: str) -> None:
        self.driver.delete_cookie(cookie_name)
