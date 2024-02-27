import pytest
from pages.login_page import LoginPage
from pages.base_page import BasePage

@pytest.mark.usefixtures("driver")
class TestLogin:
    def test_login_valid(self, driver):
        login_page = LoginPage(driver)
        login_page.enter_username("Dorzhievzhargal7@gmail.com")
        login_page.enter_password("Zhargal5678904321")
        login_page.click_login()

        # Проверка успешности входа
        assert login_page.is_login_successful(), "Вход не был успешен"



@pytest.mark.usefixtures("driver")
class TestRedirectMarketplace:
    def test_redirect_marketplace_valid(self, driver):
        login_page = LoginPage(driver)
        # Вызываем метод выполнения логина
        login_page.perform_full_login("Dorzhievzhargal7@gmail.com", "Zhargal5678904321")

        # Теперь пользователь залогинен, можно продолжать с тестом перенаправления
        marketplace_redirect = BasePage(driver)
        marketplace_redirect.redirect_to_marketplace()

        # Добавьте проверки для подтверждения успешного перенаправления на Marketplace


