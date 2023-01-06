import time
from typing import List, Any

import pytest
from pom.homepage_nav import HomepageNav


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.usefixtures('setup')
class TestHomepage:

    def test_nav_links(self):
        homepage_nav = HomepageNav(self.driver)
        # actual_links = homepage_nav.get_nav_links_text()  # результат работы алгоритма
        # expected_links = homepage_nav.NAV_LINK_TEXT  # верный результат
        # assert expected_links == actual_links, 'Validating nav links text'  # проверка

        # ниже представлен кусок кода, который поволяет найти куки, которые блокируют работу тестирования
        # ------------------------------------------------------
        # cookies = homepage_nav.driver.get_cookies()
        # cookies_names = [cookie['name'] for cookie in cookies]
        # print(cookies)
        # print('--------------')
        # print(cookies_names)
        # ------------------------------------------------------

        for index in range(13):  # 13 - потому что именно столько элементов необходимо прокликать. Строгая индексация
            homepage_nav.get_nav_links()[index].click()  # клик по ссылке