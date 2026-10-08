# Braida login BDD tests

This project uses `pytest-bdd` for Gherkin scenarios and `pytest-playwright` for browser automation.

## Setup (Windows PowerShell)

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m playwright install chromium
```

Set credentials for a dedicated test account in the current PowerShell session:

```powershell
$env:BRAIDA_EMAIL = "your-test-account@example.com"
$env:BRAIDA_PASSWORD = "your-test-password"
```

Run the scenario in a visible browser:

```powershell
pytest --headed
```

Run headlessly:

```powershell
pytest
```

The Playwright `page` fixture manages the browser and page lifecycle. Playwright `expect` assertions in `login_page.py` verify the dashboard URL and headings; the sign-out step verifies return to the login page.
