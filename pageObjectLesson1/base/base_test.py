from pageObjectLesson1.pages.login_page import LoginPage
from pageObjectLesson1.pages.contacts_page import ContactsPage


class BaseTest:

    def setup_method(self):
        self.contacts_page = ContactsPage(self.driver)
        self.login_page = LoginPage(self.driver)
