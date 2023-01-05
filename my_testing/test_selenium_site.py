# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
# # https://www.selenium.dev/documentation/webdriver/getting_started/first_script/ the first script. There is description
#
#
# def test_eight_components():
#     driver = webdriver.Chrome()  # Getting webdriver
#
#     driver.get("https://www.selenium.dev/selenium/web/web-form.html")  # URL
#
#     title = driver.title
#     assert title == "Web form"
#
#     driver.implicitly_wait(0.5)
#
#     text_box = driver.find_element(by=By.NAME, value="my-text")
#     submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
#
#     text_box.send_keys("Selenium")
#     submit_button.click()
#
#     message = driver.find_element(by=By.ID, value="message")
#     value = message.text
#     assert value == "Received!"
#
#     driver.quit()