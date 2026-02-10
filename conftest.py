import pytest
from pages.login_page import LoginPage
from utils.config import BASE_URL, APP_USERNAME, APP_PASSWORD

@pytest.fixture
def logged_in_page(page):
    """
    This fixture logs in once and returns a logged-in page
    """
    login_page = LoginPage(page)
    login_page.open(BASE_URL)
    login_page.login(APP_USERNAME, APP_PASSWORD)

    # Wait until inventory page loads
    page.wait_for_url("**/inventory.html")

    return page
