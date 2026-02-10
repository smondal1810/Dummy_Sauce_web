class CheckoutCompletePage:

    SUCCESS_MESSAGE = ".complete-header"
    BACK_HOME_BTN = "#back-to-products"

    def __init__(self, page):
        self.page = page

    def wait_for_page(self):
        self.page.wait_for_url("**/checkout-complete.html")

    def get_success_message(self):
        return self.page.text_content(self.SUCCESS_MESSAGE)

    def go_back_home(self):
        self.page.click(self.BACK_HOME_BTN)
