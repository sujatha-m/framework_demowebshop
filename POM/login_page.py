import time

from selenium import webdriver
from data import reading_excel
# from data.reading_excel import locator_data

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)

driver.get("https://demowebshop.tricentis.com/login")
driver.maximize_window()
time.sleep(2)

login_obj = reading_excel.locator_data()

class DemoLogin:
    def login_email(self):
        driver.find_element("id", "Email").send_keys("sujatha2@gmail.com")

    def login_pwd(self):
        driver.find_element("id", "Password").send_keys("password123")

    def login(self):
        driver.find_element("xpath", '(//input[@type="submit"])[2]').click()

login_obj = DemoLogin()
login_obj.login_email()
login_obj.login_pwd()
login_obj.login()

driver.close()