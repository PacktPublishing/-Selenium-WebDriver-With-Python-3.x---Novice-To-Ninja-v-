from selenium import webdriver

class RunFFTests():

    def testMethod(self):
        # Initiate the driver instance
        driver = webdriver.Firefox(
            executable_path="/Users/atomar/Documents/workspace_personal/libs/geckodriver")

        # Windows
        # driver = webdriver.Firefox(executable_path="D:\\location\\geckodriver.exe")
        driver.get("http://www.letskodeit.com")

ff = RunFFTests()
ff.testMethod()