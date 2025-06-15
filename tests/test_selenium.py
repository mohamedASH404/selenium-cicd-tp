import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class TestCalculator:
    @pytest.fixture(scope="class")
    def driver(self):
        chrome_options = Options()
        if os.getenv('CI'):
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--window-size=1920,1080')
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.implicitly_wait(10)
        yield driver
        driver.quit()

    def test_page_loads(self, driver):
        file_path = os.path.abspath("../src/index.html")
        driver.get(f"file://{file_path}")
        assert "Calculatrice Simple" in driver.title
        assert driver.find_element(By.ID, "num1").is_displayed()
        assert driver.find_element(By.ID, "num2").is_displayed()
        assert driver.find_element(By.ID, "operation").is_displayed()
        assert driver.find_element(By.ID, "calculate").is_displayed()

    def test_addition(self, driver):
        file_path = os.path.abspath("../src/index.html")
        driver.get(f"file://{file_path}")
