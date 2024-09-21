import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture()
def navi_cookies():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://engeto.cz/")
        page.wait_for_selector("#cookiescript_accept", timeout=5000)  # Počkáme na zobrazení elementu
        cookie_button = page.locator("#cookiescript_accept")  # Najdeme element pomocí jeho ID
        cookie_button.click()  # Klikneme na tlačítko
        # Po kliknutí na cookies tlačítko můžeš vrátit stránku pro další testy
        yield page
        page.close()
        # Po dokončení testů zavři prohlížeč
        browser.close()

        



def test_navi(navi_cookies):   
        page = navi_cookies
        assert page.title() == "Kurzy programování a dalších IT technologií | ENGETO" # Ověření titulku stránky 
        nadpis = page.locator("h1") # Najdeme element h1
        assert nadpis.inner_text() == "STAŇ SE NOVÝM IT TALENTEM" # Ověříme jeho text 

def test_click(navi_cookies):
        page = navi_cookies
        button = page.locator("a.block-button.size-xl.type-premium.mobile-size-l").nth(0) # Najdeme button a clickneme
        button.click()
        expected_url = "https://engeto.cz/prehled-kurzu/"         
        assert expected_url == page.url   # Ověření, že jsme byli přesměrování na očekávanou stránku 



