import pytest
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setUp")
class BaseClass:
    def selectOptionByText(self,locator,text):
        select = Select(locator)
        select.select_by_visible_text(text)