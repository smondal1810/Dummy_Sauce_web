class CheckoutOverviewPage:

    FINISH_BTN = "#finish"
    TOTAL_PRICE = ".summary_total_label"

    def __init__(self, page):
        self.page = page

    def wait_for_page(self):
        self.page.wait_for_url("**/checkout-step-two.html")

    def get_total_price(self):
        return self.page.text_content(self.TOTAL_PRICE)

    def click_finish(self):
        self.page.click(self.FINISH_BTN)
