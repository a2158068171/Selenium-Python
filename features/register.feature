Feature: Register User

@low
Scenario: Register User with valid credentials
    Given the User goes to the Website
    When the User enters with valid credentials
    Then the User is registered successfully
