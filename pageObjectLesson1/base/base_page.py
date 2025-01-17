from selenium.webdriver.chrome.webdriver import WebDriver
from pageObjectLesson1.metaclasses.meta_locator import MetaLocator


class BasePage(metaclass=MetaLocator):
    _DASHBOARD_TAB = "//a[text()='Dashboard']"
    _PROFILE_BUTTON = "//button[@aria-label='Profile']"
    _LOGOUT_BUTTON = "//ul[@role='menu']//li//div"

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def open_page(self):
        self.driver.get(self._PAGE_URL)

    def logout(self):
        self.driver.find_element(*self._PROFILE_BUTTON).click()
        self.driver.find_element(*self._LOGOUT_BUTTON).click()

    def is_opened(self):
        assert self.driver.current_url == self._PAGE_URL, f"{self._PAGE_URL} is opened instead of {self.driver.current_url}"

