from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/upload");
driver.find_element(By.ID, "file-upload").send_keys("F:/PyProjects/SeleniumTestProd/1.jpg")
driver.find_element(By.ID, "file-submit").submit()
if driver.page_source.find("File Uploaded!"):
    print("file upload success")
else:
    print("file upload not successful")
driver.quit()
