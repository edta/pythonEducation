from base.base_page import BasePage


class LoginPage(BasePage):
    _PAGE_URL = "https://release-crm.qa-playground.com/#/login"
    _USERNAME_FIELD = ("xpath", "//input[@id='username']")
    _PASSWORD_FIELD = ("xpath", "//input[@id='password']")
    _SIGN_IN_BUTTON = ('xpath', "//button[@type='submit']")

    def login(self, username, login):
        username_field = self.driver.find_element(*self._USERNAME_FIELD)
        username_field.send_keys(username)
        password_field = self.driver.find_element(*self._PASSWORD_FIELD)
        password_field.send_keys(login)
        self.driver.find_element(*self._SIGN_IN_BUTTON).click()

