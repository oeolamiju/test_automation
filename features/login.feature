@regression @login
Feature: User login
  As a registered Braida user
  I want to sign in to my account
  So that I can access my dashboard

  Scenario: A valid user signs in and signs out
    Given the user opens the sign-in page
    When the user signs in with valid credentials
    Then the dashboard is displayed
    When the user signs out
