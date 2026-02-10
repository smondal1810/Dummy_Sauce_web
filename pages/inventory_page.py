class InventoryPage:

    SORT_DROPDOWN = ".product_sort_container"
    INVENTORY_ITEMS = ".inventory_item"
    ITEM_PRICE = ".inventory_item_price"
    ADD_TO_CART_BTN = "button.btn_inventory"
    CART_ICON = ".shopping_cart_link"

    def __init__(self, page):
        self.page = page

    def wait_for_page(self):
        self.page.wait_for_selector(self.SORT_DROPDOWN)

    def sort_products(self, value: str):
        """
        value: az | za | lohi | hilo
        """
        self.page.select_option(self.SORT_DROPDOWN, value)

    def add_first_item_to_cart(self):
        self.page.locator(self.ADD_TO_CART_BTN).first.click()

    def add_last_item_to_cart(self):
        self.page.locator(self.ADD_TO_CART_BTN).last.click()

    def go_to_cart(self):
        self.page.click(self.CART_ICON)
