def test_smoke(page):
    page.goto("https://www.saucedemo.com")
    assert page.title() != ""
