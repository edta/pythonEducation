from base.base_test import BaseTest


class TestContactsPage(BaseTest):

    def test_logout_from_contacts_page(self):
        self.contacts_page.open_page()
        self.contacts_page.logout()
        self.login_page.is_opened()
        self.login_page.login('blabla', 'albalb')
