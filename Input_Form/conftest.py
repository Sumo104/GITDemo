import pytest
from selenium import webdriver

@pytest.fixture(scope='class')
def setUp(request):
    driver=webdriver.Chrome(executable_path="C:\\Users\\Sumit\\Desktop\\Chromedriver\\chromedriver.exe")
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver=driver
    yield
    driver.close()
