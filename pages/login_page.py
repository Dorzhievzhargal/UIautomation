from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input_locator = (By.ID, "email")  # Замените на реальный локатор
        self.password_input_locator = (By.ID, "pass")  # Замените на реальный локатор
        self.login_button_locator = (By.CSS_SELECTOR, "button[data-testid='royal_login_button']")

    def enter_username(self, username):
        username_input = self.driver.find_element(*self.username_input_locator)
        username_input.clear()
        username_input.send_keys(username)

    def enter_password(self, password):
        password_input = self.driver.find_element(*self.password_input_locator)
        password_input.clear()
        password_input.send_keys(password)

    def click_login(self):
        login_button = self.driver.find_element(*self.login_button_locator)
        login_button.click()

    def is_login_successful(self):
        # Метод для проверки успешного входа, возвращает True, если вход успешен
        # Например, проверка наличия элемента, доступного только после входа
        dashboard_element_locator = (By.XPATH, "//a[@aria-label='Facebook']")  # Замените на реальный локатор
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(dashboard_element_locator))
            return True
        except:
            return False

    def perform_full_login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
