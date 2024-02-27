from selenium import webdriver

class DriverFactory:
    @staticmethod
    def get_driver(browser):
        if browser == "firefox":
            return webdriver.Firefox()
        elif browser == "chrome":
            return webdriver.Chrome()
        else:
            raise ValueError("Unsupported browser")