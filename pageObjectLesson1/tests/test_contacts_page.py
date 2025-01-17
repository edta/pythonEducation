import pytest

from pageObjectLesson1.base.base_test import BaseTest


class TestContactsPage(BaseTest):

    @pytest.mark.regression
    def test_logout_from_contacts_page(self):
        self.contacts_page.open_page()
        self.contacts_page.logout()
        self.login_page.is_opened()
        self.login_page.login('blabla', 'albalb')

    # @pytest.mark.regression
    # def test_1(self):
    #     assert 1 + 2 == 3
    #
    # @pytest.mark.regression
    # def test_2(self):
    #     assert 1 + 2 == 3
    #
    # @pytest.mark.regression
    # def test_3(self):
    #     assert 1 + 2 == 3
    #
    # @pytest.mark.regression
    # def test_4(self):
    #     assert 1 + 2 == 3
    #
    # @pytest.mark.smoke
    # def test_8(self):
    #     assert 1 + 2 == 3
    #
    # @pytest.mark.smoke
    # def test_7(self):
    #     assert 1 + 2 == 3
    #
    # @pytest.mark.smoke
    # def test_6(self):
    #     assert 1 + 2 == 3
    #
    # @pytest.mark.smoke
    # def test_5(self):
    #     assert 1 + 2 == 3
    #
    # @pytest.mark.smoke
    # def test_9(self):
    #     assert 1 + 2 == 3