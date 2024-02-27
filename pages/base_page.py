from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.marketplace_cestions_locator = (By.XPATH, "//span[contains(text(), 'Marketplace')]")

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def redirect_to_marketplace(self):
        redirect_marketplace = self.driver.find_element(*self.marketplace_cestions_locator)
        redirect_marketplace.click()
        time.sleep(10)

    # Другие общие методы для работы со страницами
