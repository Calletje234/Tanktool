from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def error_message(e):
    print(f"Element could not be located Message: {e}")


class SeleniumHelpers:
    def __init__(self, driver):
        self.driver = driver

    def click(self, element, locator):
        lowcase_by = element.lower()
        if lowcase_by == "xpath":
            try:
                element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"{locator}")))
                self.driver.find_element_by_xpath(f"{locator}").click()
            except TimeoutError as e:
                print(error_message(e))
        elif lowcase_by == "id":
            try:
                element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, f"{locator}")))
                self.driver.find_element_by_id(f"{locator}").click()
            except TimeoutError as e:
                print(error_message(e))
        elif lowcase_by == "name":
            try:
                element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, f"{locator}")))
                self.driver.find_element_by_name(f"{locator}").click()
            except TimeoutError as e:
                print(error_message(e))

    def send_tekst(self, element, tekst, locator):
        lower_by = element.lower()
        if lower_by == "xpath":
            try:
                element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, f"{locator}")))
                text_element = self.driver.find_element_by_xpath(f"{locator}")
                text_element.click()
                text_element.clear()
                text_element.send_keys(tekst)
            except TimeoutError as e:
                print(error_message(e))
        elif lower_by == "id":
            try:
                element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, f"{locator}")))
                text_element = self.driver.find_element_by_id(f"{locator}")
                text_element.click()
                text_element.clear()
                text_element.send_keys(tekst)
            except TimeoutError as e:
                print(error_message(e))
        elif lower_by == "name":
            try:
                element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, f"{locator}")))
                text_element = self.driver.find_element_by_name(f"{locator}")
                text_element.click()
                text_element.clear()
                text_element.send_keys(tekst)
            except TimeoutError as e:
                print(error_message(e))

    def get_text(self, element, locator):
        lower_by = element.lower()
        if lower_by == "xpath":
            try:
                element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, f"{locator}")))
                page_text = self.driver.find_element_by_xpath(f"{locator}").text
                return page_text
            except:
                raise Exception("Exception Raised")
        elif lower_by == "id":
            try:
                element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, f"{locator}")))
                page_text = self.driver.find_element_by_id(f"{locator}").text
                return page_text
            except TimeoutError as e:
                print(error_message(e))
        elif lower_by == "name":
            try:
                element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, f"{locator}")))
                page_text = self.driver.find_element_by_name(f"{locator}").text
                return page_text
            except TimeoutError as e:
                print(error_message(e))


