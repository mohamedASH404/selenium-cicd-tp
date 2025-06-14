import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected
_
conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from webdriver
_
manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import os

class TestCalculator:
    @pytest.fixture(scope="class")
def driver(self):
"""Configuration du driver Chrome pour les tests"""
chrome
_
options = Options()

# Configuration pour environnement CI/CD
if os.getenv('CI'):
    chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--window-size=1920,1080')

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome
_
options)
driver.implicitly_
wait(10)
yield driver
driver.quit()
def test
_page
_
loads(self, driver):
"""Test 1: Vérifier que la page se charge correctement"""
file
_path = os.path.abspath("
../src/index.html")
driver.get(f"file://{file
_path}")
# Vérifier le titre
assert "Calculatrice Simple" in driver.title

 # Vérifier la présence des éléments principaux
assert driver.find_element(By.ID, "num1").is_displayed()
assert driver.find_element(By.ID, "num2").is_displayed()
assert driver.find_element(By.ID, "operation").is_displayed()
assert driver.find_element(By.ID, "calculate").is_displayed()

def test_addition(self, driver):
"""Test 2: Tester l'addition"""
file_path = os.path.abspath("../src/index.html")
driver.get(f"file://{file_path}")