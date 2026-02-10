from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.config import BASE_URL, APP_USERNAME, APP_PASSWORD

def test_cart_to_checkout_flow(page):
    # Login
    login = LoginPage(page)
    login.open(BASE_URL)
    login.login(APP_USERNAME, APP_PASSWORD)

    # Inventory
    inventory = InventoryPage(page)
    inventory.wait_for_page()
    inventory.sort_products("lohi")
    inventory.add_first_item_to_cart()
    inventory.go_to_cart()

    # Cart
    cart = CartPage(page)
    cart.wait_for_page()
    assert cart.get_cart_items_count() >= 1
    cart.click_checkout()

    # Checkout - Step One
    checkout = CheckoutPage(page)
    checkout.wait_for_page()
    checkout.fill_customer_info("Sunit", "Mondal", "700001")
    checkout.continue_checkout()

    # Assertion (next page loaded)
    assert "checkout-step-two.html" in page.url
