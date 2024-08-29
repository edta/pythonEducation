from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class TestJokes:

    USERNAME_INPUT_LOCATOR = ('xpath', "//input[@name='username']")
    PASSWORD_INPUT_LOCATOR = ('xpath', "//input[@name='password']")
    LOGIN_BUTTON_LOCATOR = ('xpath', "//button[@type='submit']")
    BUZZ_TAB_LOCATOR = ('xpath', "//span[text()='Buzz']")
    POST_INPUT_FIELD_LOCATOR = ('xpath', "//textarea[contains(@class, 'input')]")
    POST_BUTTON_LOCATOR = ('xpath', "//button[@type='submit']")
    FIRST_POST_LOCATOR = ('xpath', "(//p[contains(@class, 'body-text')])[1]")

    def setup_method(self):
        self.wait = WebDriverWait(self.driver, 30, poll_frequency=1)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/buzz/viewBuzz")
        self.wait.until(EC.element_to_be_clickable(self.USERNAME_INPUT_LOCATOR))
        self.driver.find_element(*self.USERNAME_INPUT_LOCATOR).send_keys("Admin")
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_INPUT_LOCATOR))
        self.driver.find_element(*self.PASSWORD_INPUT_LOCATOR).send_keys("admin123")
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON_LOCATOR))
        self.driver.find_element(*self.LOGIN_BUTTON_LOCATOR).click()


    def test_post_jike(self, get_joke):
        self.wait.until(EC.element_to_be_clickable(self.BUZZ_TAB_LOCATOR))
        self.driver.find_element(*self.BUZZ_TAB_LOCATOR).click()
        self.wait.until(EC.element_to_be_clickable(self.POST_INPUT_FIELD_LOCATOR))
        joke = get_joke.strip()
        self.driver.find_element(*self.POST_INPUT_FIELD_LOCATOR).send_keys(joke)
        self.wait.until(EC.element_to_be_clickable(self.POST_BUTTON_LOCATOR))
        self.driver.find_element(*self.POST_BUTTON_LOCATOR).click()
        self.driver.refresh()
        self.wait.until(EC.element_to_be_clickable(self.FIRST_POST_LOCATOR))
        assert self.driver.find_element(*self.FIRST_POST_LOCATOR).text == joke

