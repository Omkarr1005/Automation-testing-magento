from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AccountPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def logout(self):
        # Click account menu (adjust selector if needed)
        account_menu = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.action.switch")))
        account_menu.click()
        # Click Sign Out link
        sign_out_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign Out")))
        sign_out_link.click()
        # Wait for login page to appear
        self.wait.until(EC.visibility_of_element_located((By.ID, "email")))
