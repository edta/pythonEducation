from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestLoginPage:
    URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    TITLE = "OrangeHRM"
    USERNAME_LOCATOR = ("xpath", "//input[@name='username']")
    PASSWORD_LOCATOR = ("xpath", "//input[@name='password']")
    LOGIN_BUTTON_LOCATOR = ("xpath", "//button[contains(@class, 'login')]")
    USERNAME = "Admin"
    PASSWORD = "admin123"

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.URL)
        self.wait = WebDriverWait(self.driver, 30, poll_frequency=1)

    def test_title(self):
        title = self.driver.title
        assert title == self.TITLE, 'Title is incorrect'

    def test_controls_presence(self):
        username_field = self.wait.until(EC.visibility_of_element_located(self.USERNAME_LOCATOR))
        assert username_field.is_enabled(), "Username field isn't enable"

        password_field = self.wait.until(EC.visibility_of_element_located(self.PASSWORD_LOCATOR))
        assert password_field.is_enabled(), "Password field isn't enable"

        login_button = self.wait.until(EC.visibility_of_element_located(self.LOGIN_BUTTON_LOCATOR))
        assert login_button.is_enabled(), "Login button isn't enable"

    def test_login(self):
        username_field = self.wait.until(EC.visibility_of_element_located(self.USERNAME_LOCATOR))
        username_field.send_keys(self.USERNAME)
        password_field = self.wait.until(EC.visibility_of_element_located(self.PASSWORD_LOCATOR))
        password_field.send_keys(self.PASSWORD)
        login_button = self.wait.until(EC.visibility_of_element_located(self.LOGIN_BUTTON_LOCATOR))
        login_button.click()

        assert "dashboard" in self.driver.current_url

    def teardown_method(self):
        self.driver.close()
