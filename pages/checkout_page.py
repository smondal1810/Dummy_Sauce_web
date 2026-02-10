class CheckoutPage:

    FIRST_NAME = "#first-name"
    LAST_NAME = "#last-name"
    POSTAL_CODE = "#postal-code"
    CONTINUE_BTN = "#continue"

    def __init__(self, page):
        self.page = page

    def wait_for_page(self):
        self.page.wait_for_url("**/checkout-step-one.html")

    def fill_customer_info(self, first, last, zip_code):
        self.page.fill(self.FIRST_NAME, first)
        self.page.fill(self.LAST_NAME, last)
        self.page.fill(self.POSTAL_CODE, zip_code)

    def continue_checkout(self):
        self.page.click(self.CONTINUE_BTN)
