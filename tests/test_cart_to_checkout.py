from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage

def test_cart_to_checkout(logged_in_page):
    page = logged_in_page   # alias for clarity

    # Inventory
    inventory = InventoryPage(page)
    inventory.wait_for_page()
    inventory.sort_products("lohi")
    inventory.add_first_item_to_cart()
    inventory.go_to_cart()

    # Cart
    cart = CartPage(page)
    cart.wait_for_page()
    cart.click_checkout()

    # Checkout - Step One
    checkout = CheckoutPage(page)
    checkout.wait_for_page()
    checkout.fill_customer_info("Sunit", "Mondal", "700001")
    checkout.continue_checkout()

    # Checkout - Step Two
    overview = CheckoutOverviewPage(page)
    overview.wait_for_page()
    overview.click_finish()

    # Checkout Complete
    complete = CheckoutCompletePage(page)
    complete.wait_for_page()

    assert "Thank you for your order!" in complete.get_success_message()
