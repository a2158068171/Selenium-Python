from .base_actions import BaseActions
from pages.pages_objects.register import Register


class RegisterActions(BaseActions):

    def __init__(self, driver):
        super().__init__(driver)

    def type_user(self, user: str):
        self.type_info(Register.userInput, user)

    def type_email(self, email: str):
        self.type_info(Register.emailInput, email)

    def type_age(self, age: str):
        self.type_info(Register.ageInput, age)

    def click_to_register(self):
        self.element_click(Register.registerButton)
    
    def user_is_logged(self) -> bool:
        return self.is_displayed(Register.userRegisteredMessage)
