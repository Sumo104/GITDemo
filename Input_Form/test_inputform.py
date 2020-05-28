import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

from FormTestData.HomeTestData import HomeTestData
from PageObject.Form import PageObject
from Utility.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_fillform(self,getData):
        pageobject= PageObject(self.driver)
        pageobject.empName().send_keys(getData["Name"])
        pageobject.empEmail().send_keys(getData["Email"])
        pageobject.empPassword().send_keys(getData["Password"])
        pageobject.empCheckbox().click()
        self.selectOptionByText(pageobject.selectGender(), getData["Gender"])
        pageobject.empStatus().click()
        action=ActionChains(self.driver)
        action.move_to_element(pageobject.dOB())
        pageobject.submitBtn().click()
        assert "Success!" in pageobject.successAlert().text
        self.driver.refresh()

    @pytest.fixture(params=HomeTestData.formdata)
    def getData(self,request):
        return request.param

