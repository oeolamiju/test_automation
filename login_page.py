from playwright.sync_api import expect


class LoginPage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto("https://www.braida.co.uk/login")

    def login(self, email, password):
        self.page.get_by_role("textbox", name="Email address").fill(email)
        self.page.get_by_role("textbox", name="Email address").press("Tab")
        self.page.locator("div").filter(
            has_text="BraidaBeauty that understands"
        ).nth(5).click()
        self.page.get_by_role("textbox", name="Password").fill(password)
        self.page.get_by_role("button", name="Sign In", exact=True).click()

    def verify_dashboard(self):
        expect(self.page).to_have_url("https://www.braida.co.uk/dashboard")
        expect(self.page.get_by_role("heading", name="AI Recommendations")).to_be_visible()
        expect(self.page.get_by_role("heading", name="Application Under Review")).to_be_visible()

    def logout(self):
        self.page.get_by_role("button", name="Sign out").click()