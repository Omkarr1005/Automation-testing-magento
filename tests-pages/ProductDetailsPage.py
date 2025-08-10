from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductDetailsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.color_options = (By.CSS_SELECTOR, ".swatch-option.color")
        self.size_options = (By.CSS_SELECTOR, ".swatch-option.text")
        self.add_to_cart_btn = (By.ID, "product-addtocart-button")

    def select_size(self, size_label=None):
        """
        Select a size option by label (e.g., "32", "33", "34").
        If no size_label is provided, selects first available size.
        """
        try:
            size_elements = self.wait.until(
                EC.presence_of_all_elements_located(self.size_options)
            )
            if not size_elements:
                print("ℹ No size options found.")
                return

            if size_label:
                for elem in size_elements:
                    if elem.get_attribute("option-label") == size_label:
                        elem.click()
                        print(f"✅ Selected size: {size_label}")
                        return
                print(f"❌ Size '{size_label}' option not found, selecting first available.")
            size_elements[0].click()
            print("✅ Selected first available size.")
        except Exception as e:
            print(f"❌ Error selecting size: {e}")

    def select_color(self, color_label=None):
        """
        Select a color option by label (e.g., "Black", "Red").
        If no color_label is provided, selects first available color.
        """
        try:
            color_elements = self.wait.until(
                EC.presence_of_all_elements_located(self.color_options)
            )
            if not color_elements:
                print("ℹ No color options found.")
                return

            if color_label:
                for elem in color_elements:
                    if elem.get_attribute("option-label") == color_label:
                        elem.click()
                        print(f"✅ Selected color: {color_label}")
                        return
                print(f"❌ Color '{color_label}' option not found, selecting first available.")
            color_elements[0].click()
            print("✅ Selected first available color.")
        except Exception as e:
            print(f"❌ Error selecting color: {e}")

    def add_to_cart(self):
        """
        Click the Add to Cart button and wait for success confirmation.
        """
        try:
            add_button = self.wait.until(
                EC.element_to_be_clickable(self.add_to_cart_btn)
            )
            add_button.click()
            # Wait for success message after adding to cart
            self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "div.message-success"))
            )
            print("✅ Product added to cart successfully.")
        except Exception as e:
            print(f"❌ Failed to add product to cart: {e}")

    def verify_item_in_cart(self):
        """
        Verify if the item was added to the cart by checking success message or cart count.
        """
        try:
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.message-success")))
            cart_count = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "span.counter-number"))
            )
            if int(cart_count.text) > 0:
                print(f"✅ Cart has {cart_count.text} item(s).")
                return True
            else:
                print("❌ Cart counter is zero.")
                return False
        except Exception as e:
            print(f"❌ Failed to verify item in cart: {e}")
            return False
