from base.base_page import BasePage


class ContactsPage(BasePage):
    _PAGE_URL = "https://release-crm.qa-playground.com/#/contacts"

    def add_new_contact(self):
        ...