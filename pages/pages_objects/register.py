from selenium.webdriver.common.by import By

class Register:
    userInput = (By.XPATH, "//input[@name='name']")
    emailInput = (By.XPATH, "//input[@name='email']")
    ageInput = (By.XPATH, "//input[@id='ageSlider']")
    registerButton = (By.XPATH, "//input[@type='submit']")
    userRegisteredMessage = (By.XPATH, "//*[@id='formMessage']")
