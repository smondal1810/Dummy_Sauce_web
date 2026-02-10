from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.config import BASE_URL, APP_USERNAME, APP_PASSWORD

def test_sort_by_price_low_to_high_and_add_item(page):
    # Login
    login = LoginPage(page)
    login.open(BASE_URL)
    login.login(APP_USERNAME, APP_PASSWORD)

    # Inventory
    inventory = InventoryPage(page)
    inventory.wait_for_page()

    # Sort by Price (low to high)
    inventory.sort_products("lohi")

    # Add cheapest item (first item after sorting)
    inventory.add_first_item_to_cart()
    inventory.go_to_cart()

    # Assertion
    assert "cart.html" in page.url
