"""import pytest
from selenium import webdriver
from config import BASE_URL, CHROME_DRIVER_PATH

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from config import BASE_URL

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--disable-notifications")  # Отключение уведомлений
    options.add_argument("--disable-geolocation")  # Отключение геолокации
    # Добавьте другие аргументы командной строки для отключения нежелательных функций

    service = Service(ChromeDriverManager().install())  # Используйте Service для передачи пути к драйверу

    # Инициализируйте драйвер с указанными опциями и сервисом
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(BASE_URL)
    driver.implicitly_wait(10)  # Настройте неявное ожидание
    yield driver  # Верните драйвер для использования в тестах
    driver.quit()  # Закройте браузер после выполнения теста
