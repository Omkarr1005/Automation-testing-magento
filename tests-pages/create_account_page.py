from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CreateAccountPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_create_account_page(self):
        self.driver.get("https://magento2demo.firebearstudio.com/customer/account/create/")

    def enter_firstname(self, firstname):
        elem = self.wait.until(EC.visibility_of_element_located((By.ID, "firstname")))
        elem.clear()
        elem.send_keys(firstname)

    def enter_lastname(self, lastname):
        elem = self.wait.until(EC.visibility_of_element_located((By.ID, "lastname")))
        elem.clear()
        elem.send_keys(lastname)

    def enter_email(self, email):
        elem = self.wait.until(EC.visibility_of_element_located((By.ID, "email_address")))
        elem.clear()
        elem.send_keys(email)

    def enter_password(self, password):
        elem = self.wait.until(EC.visibility_of_element_located((By.ID, "password")))
        elem.clear()
        elem.send_keys(password)

    def enter_password_confirmation(self, password):
        elem = self.wait.until(EC.visibility_of_element_located((By.ID, "password-confirmation")))
        elem.clear()
        elem.send_keys(password)

    def submit_form(self):
        submit_btn = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.action.submit.primary")))
        submit_btn.click()
