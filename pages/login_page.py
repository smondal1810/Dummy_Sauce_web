class LoginPage:

    USERNAME = "#user-name"
    PASSWORD = "#password"
    LOGIN_BTN = "#login-button"
    ERROR_MSG = "[data-test='error']"

    def __init__(self, page):
        self.page = page

    def open(self, url):
        self.page.goto(url)

    def login(self, username, password):
        self.page.fill(self.USERNAME, username)
        self.page.fill(self.PASSWORD, password)
        self.page.click(self.LOGIN_BTN)

    def get_error_message(self):
        return self.page.text_content(self.ERROR_MSG)
