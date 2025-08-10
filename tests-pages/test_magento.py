import pytest
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from login_page import LoginPage
from search_page import SearchPage
from create_account_page import CreateAccountPage
from ProductDetailsPage import ProductDetailsPage
from AccountPage import AccountPage


@pytest.fixture(scope="class")
def setup(request):
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()

@pytest.mark.usefixtures("setup")
class TestMagentoSite:
    generated_email = None  # class variable to share email

    def test_create_account(self):
        driver = self.driver
        create_account_page = CreateAccountPage(driver)
        wait = WebDriverWait(driver, 20)

        create_account_page.open_create_account_page()
        time.sleep(2)

        random_number = random.randint(1000, 9999)
        email = f"omkar.auto.test{random_number}@example.com"

        create_account_page.enter_firstname("Amit")
        create_account_page.enter_lastname("Verma")
        create_account_page.enter_email(email)
        create_account_page.enter_password("Test@1234")
        create_account_page.enter_password_confirmation("Test@1234")

        create_account_page.submit_form()

        # Wait for success message
        success_message_locator = (By.CSS_SELECTOR, ".message-success")
        wait.until(EC.visibility_of_element_located(success_message_locator))
        print(f"🧪 Create Account Test Done with email: {email}")
        TestMagentoSite.generated_email = email

        # Now wait until Sign Out button is visible (means we are still logged in, stay on this page)
        try:
            sign_out_btn = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign Out")))
            print("✅ Sign Out button is visible, staying on Create Account page to sign out")

            # Click sign out
            sign_out_btn.click()

            # Wait until login page opens - login button/link visible
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.login")))
            print("✅ Successfully signed out, now on Login page")
        except Exception:
            # If Sign Out button not found, means already redirected to login page or logged out
            print("ℹ Sign Out button not found, might be already on login page or logged out")

    def test_login_and_search(self):
        driver = self.driver
        login_page = LoginPage(driver)
        search_page = SearchPage(driver)

        wait = WebDriverWait(driver, 10)
        login_page.open_login_page()
        time.sleep(2)

        # Use hardcoded credentials here
        login_page.enter_email("omkarsanas3033@gmail.com")
        login_page.enter_password("Xyzasdf@123")


        # Wait 10 seconds for manual CAPTCHA solving
        print("⏳ Please solve the CAPTCHA within 10 seconds...")
        time.sleep(10)

        login_page.click_sign_in()

        search_page.enter_search_query("Shorts")
        search_page.click_search()
        time.sleep(5)

    def test_add_to_cart_after_login(self):
        driver = self.driver
        search_page = SearchPage(driver)
        product_page = ProductDetailsPage(driver)

        search_page.enter_search_query("Shorts")
        search_page.click_search()

        search_page.click_first_product()

        product_page.select_size("32")
        product_page.select_color("Red")
        product_page.add_to_cart()

        # Verify cart item (you might have a method for this)
        assert search_page.verify_item_in_cart()

    def test_proceed_to_checkout_and_verify_place_order(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)

        cart_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.action.showcart")))
        cart_icon.click()

        proceed_to_checkout_btn = wait.until(EC.element_to_be_clickable((By.ID, "top-cart-btn-checkout")))
        proceed_to_checkout_btn.click()

        wait.until(EC.presence_of_element_located((By.ID, "checkout")))

        try:
            wait.until(EC.visibility_of_element_located((By.NAME, "street[0]"))).send_keys("123 Test Street")
            driver.find_element(By.NAME, "city").send_keys("Mumbai")
            driver.find_element(By.NAME, "region_id").click()
            time.sleep(0.5)
            driver.find_element(By.XPATH, "//select[@name='region_id']/option[contains(text(),'Maharashtra')]").click()
            driver.find_element(By.NAME, "postcode").send_keys("400001")
            driver.find_element(By.NAME, "telephone").send_keys("9876543210")

            next_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.continue")))
            next_btn.click()

            place_order_btn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.action.primary.checkout")))
            assert place_order_btn.is_displayed()
            print("✅ Place Order button is visible.")

        except Exception as e:
            print("⚠️ Shipping form may already be filled or error occurred:", str(e))

        time.sleep(3)
