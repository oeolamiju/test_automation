import os

import pytest
from pytest_bdd import given, parsers, scenarios, then, when
from playwright.sync_api import Page, expect

from login_page import LoginPage


scenarios("features/login.feature")


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)


@given("the user opens the sign-in page")
def open_sign_in_page(login_page: LoginPage) -> None:
    login_page.open()


@when("the user signs in with valid credentials")
def sign_in_with_valid_credentials(login_page: LoginPage) -> None:
    email = os.getenv("BRAIDA_EMAIL")
    password = os.getenv("BRAIDA_PASSWORD")
    if not email or not password:
        raise RuntimeError(
            "Set BRAIDA_EMAIL and BRAIDA_PASSWORD environment variables before running this scenario."
        )

    login_page.login(email, password)


@then("the dashboard is displayed")
def dashboard_is_displayed(login_page: LoginPage) -> None:
    login_page.verify_dashboard()


@when(parsers.parse("the user signs out"))
def sign_out(login_page: LoginPage) -> None:
    login_page.logout()
    expect(login_page.page).to_have_url("https://www.braida.co.uk/")
    expect(login_page.page.get_by_role("link", name="Log in")).to_be_visible()
