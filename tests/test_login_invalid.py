from pages.login_page import LoginPage
from utils.config import BASE_URL

def test_login_invalid_credentials(page):
    login_page = LoginPage(page)

    login_page.open(BASE_URL)
    login_page.login("wrong_user", "wrong_password")

    error_message = login_page.get_error_message()
    assert "Username and password do not match" in error_message
