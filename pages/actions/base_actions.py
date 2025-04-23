from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BaseActions:

    def __init__(self, driver):
        self.driver = driver

    def load(self,url):
        self.driver.get(url)

    def _wait_for_element(self, by_locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(by_locator)
            )
            return self.driver.find_element(*by_locator)
        except TimeoutException:
            print ("The element was not found")
            return None

    def element_click(self, by_locator):
        user = self._wait_for_element(by_locator)
        if user:
            user.click()
        else:
            raise Exception("Can't click on the element")
    
    def type_info(self, by_locator, keyword):
        user = self._wait_for_element(by_locator)
        if user:
            user.send_keys(keyword)
        else:
            raise Exception("Can't click on the element")
        
    def is_displayed(self, by_locator) -> bool:
        user = self._wait_for_element(by_locator)
        if user:
            user.is_displayed()
        else:
            return False

    def is_enabled(self, by_locator) -> bool:
        user = self._wait_for_element(by_locator)
        if user:
            user.is_enabled()
        else:
            return False   