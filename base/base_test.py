from pages.login_page import LoginPage
from pages.contacts_page import ContactsPage


class BaseTest:

    def setup_method(self):
        self.contacts_page = ContactsPage(self.driver)
        self.login_page = LoginPage(self.driver)
