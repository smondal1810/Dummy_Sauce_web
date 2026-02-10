class CartPage:

    CART_ITEM = ".cart_item"
    CHECKOUT_BTN = "#checkout"
    CONTINUE_SHOPPING_BTN = "#continue-shopping"

    def __init__(self, page):
        self.page = page

    def wait_for_page(self):
        self.page.wait_for_url("**/cart.html")

    def get_cart_items_count(self):
        return self.page.locator(self.CART_ITEM).count()

    def click_checkout(self):
        self.page.click(self.CHECKOUT_BTN)
