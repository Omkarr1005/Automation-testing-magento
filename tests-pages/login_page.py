from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_login_page(self):
        self.driver.get("https://magento2demo.firebearstudio.com/customer/account/login/referer/aHR0cHM6Ly9tYWdlbnRvMmRlbW8uZmlyZWJlYXJzdHVkaW8uY29tLw~~/")

    def enter_email(self, email):
        email_input = self.wait.until(EC.visibility_of_element_located((By.ID, "email")))
        email_input.clear()
        email_input.send_keys(email)

    def enter_password(self, password):
        password_input = self.wait.until(EC.visibility_of_element_located((By.ID, "pass")))
        password_input.clear()
        password_input.send_keys(password)

    def click_sign_in(self):
        sign_in_button = self.wait.until(EC.element_to_be_clickable((By.ID, "send2")))
        sign_in_button.click()
