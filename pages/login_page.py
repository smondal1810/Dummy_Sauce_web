from utils.logger import get_logger

class LoginPage:

    USERNAME = "#user-name"
    PASSWORD = "#password"
    LOGIN_BTN = "#login-button"
    ERROR_MSG = "[data-test='error']"

    def __init__(self, page):
        self.page = page
        self.logger = get_logger(self.__class__.__name__)

    def open(self, url):
        self.logger.info(f"Opening login page: {url}")
        self.page.goto(url)

    def login(self, username, password):
        self.logger.info(f"Entering username: {username}")
        self.page.fill(self.USERNAME, username)

        self.logger.info("Entering password")
        self.page.fill(self.PASSWORD, password)

        self.logger.info("Clicking login button")
        self.page.click(self.LOGIN_BTN)

    def get_error_message(self):
        self.logger.info("Fetching login error message")
        return self.page.text_content(self.ERROR_MSG)
