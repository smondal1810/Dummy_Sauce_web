from pages.login_page import LoginPage
from utils.config import BASE_URL, APP_USERNAME, APP_PASSWORD

def test_login_success(page):
    login_page = LoginPage(page)

    login_page.open(BASE_URL)
    login_page.login(APP_USERNAME, APP_PASSWORD)

    assert "inventory" in page.url
