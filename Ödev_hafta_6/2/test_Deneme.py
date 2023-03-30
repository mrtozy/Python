from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pytest
from datetime import date
from pathlib import Path
from selenium.webdriver.common.action_chains import ActionChains
import constants 





class Test_sauce:
   
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(constants.URL)
        self.folder_path = str(date.today())
        Path(self.folder_path).mkdir(exist_ok=True)

    
    def teardown_method(self):
        self.driver.quit()

    
    def wait_for_element_visible(self, locator, timeout=5):
        WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))

   
    def test_about(self):
        self.test_valid_login("standard_user", "secret_sauce")

        self.wait_for_element_visible((By.ID, constants.menu_btn_id))
        menu_btn = self.driver.find_element(By.ID, constants.menu_btn_id)
        menu_btn.click()

        self.wait_for_element_visible((By.ID, constants.about_btn_id))
        self.driver.find_element(By.ID, constants.about_btn_id).click()

        screenshot_file_path = str(Path(self.folder_path) / f"test-about-page.png")
        self.driver.save_screenshot(screenshot_file_path)

        assert self.driver.current_url == constants.saucelab_about_url

    
    @pytest.mark.parametrize("username,password", [("locked_out_user", "secret_sauce")])
    def test_banned_account(self, username, password):
        self.wait_for_element_visible((By.ID, constants.user_id))
        name_input = self.driver.find_element(By.ID, constants.user_id)

        self.wait_for_element_visible((By.ID, constants.password_id))
        password_input = self.driver.find_element(By.ID, constants.password_id)

        action = ActionChains(self.driver)
        action.send_keys_to_element(name_input, username)
        action.send_keys_to_element(password_input, password)
        action.perform()

        login_btn = self.driver.find_element(By.ID, constants.login_id)
        login_btn.click()

        self.wait_for_element_visible((By.XPATH, constants.error_msg_box_full_path))
        error_msg = self.driver.find_element(By.XPATH, constants.error_msg_box_full_path)

        screenshot_file_path = str(Path(self.folder_path) / f"test-banned-account-{username}-{password}.png")
        self.driver.save_screenshot(screenshot_file_path)

        assert error_msg.text == constants.banned_account_message

    
    @pytest.mark.parametrize("username,password", [("1", "1"), ("kodlama.io", "123")])
    def test_invalid_login(self, username, password):
        self.wait_for_element_visible((By.ID, constants.user_id))
        name_input = self.driver.find_element(By.ID, constants.user_id)

        self.wait_for_element_visible((By.ID, constants.password_id))
        password_input = self.driver.find_element(By.ID, constants.password_id)

        action = ActionChains(self.driver)
        action.send_keys_to_element(name_input, username)
        action.send_keys_to_element(password_input, password)
        action.perform()

        login_btn = self.driver.find_element(By.ID, constants.login_id)
        login_btn.click()

        self.wait_for_element_visible((By.XPATH, constants.error_msg_box_full_path))
        error_msg = self.driver.find_element(By.XPATH, constants.error_msg_box_full_path)

        screenshot_file_path = str(Path(self.folder_path) / f"test-invalid-login-{username}-{password}.png")
        self.driver.save_screenshot(screenshot_file_path)

        assert error_msg.text == constants.unmatched_username_password_text

    
    def test_just_click_login(self):
        self.wait_for_element_visible((By.ID, constants.login_id))
        login_btn = self.driver.find_element(By.ID, constants.login_id)
        login_btn.click()

        self.wait_for_element_visible((By.XPATH, constants.error_msg_box_full_path))
        error_msg = self.driver.find_element(By.XPATH, constants.error_msg_box_full_path)

        screenshot_file_path = str(Path(self.folder_path) / f"test-only-click-login.png")
        self.driver.save_screenshot(screenshot_file_path)

        assert error_msg.text == constants.just_clik_message

    
    @pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce")])
    def test_valid_login(self, username, password):
        self.wait_for_element_visible((By.ID, constants.user_id))
        username_input = self.driver.find_element(By.ID, constants.user_id)
        username_input.click()
        username_input.send_keys(username)

        self.wait_for_element_visible((By.ID, constants.password_id))
        password_input = self.driver.find_element(By.ID, constants.password_id)
        password_input.click()
        password_input.send_keys(password)
        self.wait_for_element_visible((By.ID, constants.login_id))
        self.driver.find_element(By.ID, constants.login_id).click()

        screenshot_file_path = str(Path(self.folder_path) / f"test-valid-login-{username}-{password}.png")
        self.driver.save_screenshot(screenshot_file_path)

        assert self.driver.current_url == constants.product_list_url

   
    def test_logout(self):
        self.test_valid_login("standard_user", "secret_sauce")

        self.wait_for_element_visible((By.ID, constants.menu_btn_id))
        menu_btn = self.driver.find_element(By.ID, constants.menu_btn_id)
        menu_btn.click()

        self.wait_for_element_visible((By.ID, constants.logout_btn_id))
        logout_btn = self.driver.find_element(By.ID, constants.logout_btn_id)

        screenshot_file_path = str(Path(self.folder_path) / f"test-logout.png")
        self.driver.save_screenshot(screenshot_file_path)

        logout_btn.click()

        assert self.driver.current_url == constants.URL

                                     

   
    @pytest.mark.parametrize("username,password", [("problem_user", "secret_sauce")])
    def test_problem_user(self, username, password):
        self.wait_for_element_visible((By.ID, constants.user_id))
        username_input = self.driver.find_element(By.ID, constants.user_id)
        username_input.click()
        username_input.send_keys(username)
        self.wait_for_element_visible((By.ID, constants.password_id))
        password_input = self.driver.find_element(By.ID, constants.password_id)
        password_input.click()
        password_input.send_keys(password)
        self.wait_for_element_visible((By.ID, constants.login_id))
        self.driver.find_element(By.ID, constants.login_id).click()
        screenshot_file_path = str(Path(self.folder_path) / f"test-problem-user-{username}-{password}.png")
        self.driver.save_screenshot(screenshot_file_path)
        assert self.driver.current_url == constants.product_list_url

    
    def test_urun_say(self):
        total_product = 6
        self.test_valid_login("standard_user", "secret_sauce")
        self.wait_for_element_visible((By.CLASS_NAME, constants.item_class_name))
        list_product = self.driver.find_elements(By.CLASS_NAME, constants.item_class_name)
        screenshot_file_path = str(Path(self.folder_path) / f"test-test_urun_say.png")
        self.driver.save_screenshot(screenshot_file_path)
        assert len(list_product) == total_product

   
    def test_x_icon(self):
        self.wait_for_element_visible((By.ID, constants.login_id))
        login_button = self.driver.find_element(By.ID, constants.login_id)
        login_button.click()
        error_button = self.driver.find_element(By.CLASS_NAME, constants.error_btn_id)
        screenshot_file_path = str(Path(self.folder_path) / f"test-error-icon.png")
        self.driver.save_screenshot(screenshot_file_path)
        error_icon = len(self.driver.find_elements(By.CLASS_NAME, constants.error_icon_class_name))
        error_button.click()
        assert error_icon > 0

    
    def test_z_a(self):
        self.test_valid_login("standard_user", "secret_sauce")
        self.wait_for_element_visible((By.CLASS_NAME, constants.item_class_name))
        self.wait_for_element_visible((By.CLASS_NAME, constants.order_menu_class_name))
        order_opt = self.driver.find_element(By.CLASS_NAME, constants.order_menu_class_name)
        order_opt.click()
        self.wait_for_element_visible((By.XPATH, constants.sorting_z_to_a_full_path))
        z_a = self.driver.find_element(By.XPATH, constants.sorting_z_to_a_full_path)
        z_a.click()
        screenshot_file_path = str(Path(self.folder_path) / f"test-z-a.png")
        self.driver.save_screenshot(screenshot_file_path)

    def test_low_high(self):
        self.test_valid_login("standard_user", "secret_sauce")
        self.wait_for_element_visible((By.CLASS_NAME, constants.item_class_name))
        self.wait_for_element_visible((By.CLASS_NAME, constants.order_menu_class_name))
        order_opt = self.driver.find_element(By.CLASS_NAME, constants.order_menu_class_name)
        order_opt.click()
        self.wait_for_element_visible((By.XPATH, constants.low_high))
        low_high = self.driver.find_element(By.XPATH, constants.low_high)
        low_high.click()
        screenshot_file_path = str(Path(self.folder_path) / f"test-low-high.png")
        self.driver.save_screenshot(screenshot_file_path)  

    def test_high_low(self):
        self.test_valid_login("standard_user", "secret_sauce")
        self.wait_for_element_visible((By.CLASS_NAME, constants.item_class_name))
        self.wait_for_element_visible((By.CLASS_NAME, constants.order_menu_class_name))
        order_opt = self.driver.find_element(By.CLASS_NAME, constants.order_menu_class_name)
        order_opt.click()
        self.wait_for_element_visible((By.XPATH, constants.high_low))
        high_low = self.driver.find_element(By.XPATH, constants.high_low)
        high_low.click()
        screenshot_file_path = str(Path(self.folder_path) / f"test-high-low.png")
        self.driver.save_screenshot(screenshot_file_path)          
      
    def test_rest_kart(self):
        self.test_valid_login("standard_user", "secret_sauce")
        self.wait_for_element_visible((By.ID, constants.add_cart_btn_id))
        add_cart_btn1 = self.driver.find_element(By.ID, constants.add_cart_btn_id)
        add_cart_btn1.click()
        self.wait_for_element_visible((By.ID, constants.menu_btn_id))
        self.driver.find_element(By.ID, constants.menu_btn_id).click()
        self.wait_for_element_visible((By.ID, constants.reset_sidebar_link))
        self.driver.find_element(By.ID, constants.reset_sidebar_link).click()
        screenshot_file_path = str(Path(self.folder_path) / f"test-rest-kart.png")
        self.driver.save_screenshot(screenshot_file_path)
        
  
    def test_kart(self):
        self.test_valid_login("standard_user", "secret_sauce")
        self.wait_for_element_visible((By.ID, constants.add_cart_btn_id))
        add_cart_btn1 = self.driver.find_element(By.ID, constants.add_cart_btn_id)
        add_cart_btn1.click()
        self.wait_for_element_visible((By.ID, constants.add_to_cart_sauce_labs_fleece_jacket))
        add_cart_btn2 = self.driver.find_element(By.ID, constants.add_to_cart_sauce_labs_fleece_jacket)
        add_cart_btn2.click()
        see_cart = self.driver.find_element(By.CLASS_NAME, constants.see_cart_id)
        see_cart.click()
        screenshot_file_path = str(Path(self.folder_path) / f"test-kart.png")
        self.driver.save_screenshot(screenshot_file_path)
        assert self.driver.current_url == constants.cart_url

    

   
    
   



 

   
