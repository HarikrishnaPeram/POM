#from selenium.webdriver.chrome.service import Service
#service_obj= Service("C:/Users/selenium/work space/chromedriver.exe")
#driver = webdriver.Chrome(service = service_obj)
#driver.get("https://www.facebook.com/signup")
#driver.maximize_window()
import pytest

from Baseclass import BaseClass
from Signup import SignUp

@pytest.mark.usefixtures("setup")
class Testsample(BaseClass):
    def test_etoe(self):
        SignUp(self.driver)


