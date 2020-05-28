from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class PageObject:

    def __init__(self,driver):
        self.driver=driver

    name=(By.NAME,"name")
    email=(By.NAME,"email")
    password=(By.CSS_SELECTOR,"#exampleInputPassword1")
    checkbox=(By.CSS_SELECTOR,"#exampleCheck1")
    selectgender=(By.CSS_SELECTOR,"#exampleFormControlSelect1")
    empstatus=(By.ID,"inlineRadio2")
    dob=(By.NAME,"bday")
    submitbtn=(By.CSS_SELECTOR,".btn-success")
    success=(By.CSS_SELECTOR,".alert")

    def empName(self):
        return self.driver.find_element(*PageObject.name)

    def empEmail(self):
        return self.driver.find_element(*PageObject.email)

    def empPassword(self):
        return self.driver.find_element(*PageObject.password)

    def empCheckbox(self):
        return self.driver.find_element(*PageObject.checkbox)

    def selectGender(self):
        return self.driver.find_element(*PageObject.selectgender)
    def empStatus(self):
        return self.driver.find_element(*PageObject.empstatus)

    def submitBtn(self):
        return self.driver.find_element(*PageObject.submitbtn)
    def successAlert(self):
        return self.driver.find_element(*PageObject.success)

    def dOB(self):
        return self.driver.find_element(*PageObject.dob)

