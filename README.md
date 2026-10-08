# Braida login BDD tests

This project uses `pytest-bdd` for Gherkin scenarios and `pytest-playwright` for browser automation.
Allure can be used to create a browsable report of test runs.

## Setup (Windows PowerShell)

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m playwright install chromium
```

Install the pytest Allure adapter in the active virtual environment:

```powershell
python -m pip install allure-pytest
```

The Allure command-line tool also requires Java. Install Allure CLI and Java, then check that both commands work:

```powershell
java -version
allure --version
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

## Allure reports

Run the tests and write Allure result files to `allure-results`:

```powershell
pytest --alluredir=allure-results --clean-alluredir --headed
```

Open an interactive report locally:

```powershell
allure serve allure-results
```

Alternatively, generate a static report in `allure-report` and open it:

```powershell
allure generate allure-results --clean -o allure-report
allure open allure-report
```

## Sharing a report on GitHub Pages

`allure serve` is a local server; other people cannot access it. To publish a report, configure GitHub Pages to deploy an Allure report from a GitHub Actions workflow. **A Pages deployment workflow is not currently included in this repository.**

For a CI workflow, add `BRAIDA_EMAIL` and `BRAIDA_PASSWORD` as repository Actions secrets under **Settings → Secrets and variables → Actions**. The workflow should pass those secrets to pytest, generate the Allure report, and deploy the generated report to GitHub Pages. Do not put credentials in a feature file, workflow source, or committed `.env` file.

This repository is public, so assume any published report is public. Review reports and attachments for credentials, personal data, screenshots, and other sensitive information before publishing.

The Playwright `page` fixture manages the browser and page lifecycle. Playwright `expect` assertions in `login_page.py` verify the dashboard URL and headings; the sign-out step verifies return to the login page.
