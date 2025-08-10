from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_search_query(self, query):
        search_input = self.wait.until(EC.presence_of_element_located((By.ID, "search")))
        search_input.clear()
        search_input.send_keys(query)

    def click_search(self):
        search_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.action.search")))
        search_button.click()

    def click_first_product(self):
        product = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "li.product-item a.product-item-link")))
        product.click()

    def verify_item_in_cart(self):
        try:
            # Wait for success message visible after add to cart
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.message-success")))
            # Optionally check the cart count if needed
            return True
        except:
            return False
