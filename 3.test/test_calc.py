import pytest
from playwright.sync_api import sync_playwright
from playwright.sync_api import Error


@pytest.fixture()
def navi_cookies():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://www.bodymassindex.cz/")
        page.wait_for_selector("p.fc-button-label", timeout=5000)  # Počkáme na zobrazení elementu
        cookie_button = page.locator("p.fc-button-label").nth(0)  # Najdeme element pomocí jeho ID
        cookie_button.click()  # Klikneme na tlačítko
        # Po kliknutí na cookies tlačítko můžeš vrátit stránku pro další testy
        yield page
        page.close()
        # Po dokončení testů zavři prohlížeč
        browser.close()

def test_bmi(navi_cookies):
    page = navi_cookies
    vyska = page.locator("#frm-calcForm-BMI_Vyska") # Najdeme formulář a vyplníme do něj výšku 
    vyska.fill("165")
    vaha = page.locator("#frm-calcForm-BMI_Vaha") # Najdeme formulář a vyplníme váhu 
    vaha.fill("58")
    button = page.locator("button") # Najdeme a clickneme na button s odesláním hodnot 
    button.click()
    vysledek = page.locator('div.calc-result-head span:nth-of-type(3)').inner_text() # Najdeme element kam se napsal výsledek
    assert vysledek == "21.3"   # Ověření správného výsledku 

def test_invalid_bmi_input(navi_cookies):
    page = navi_cookies
    # Zkusíme vyplnit neplatný vstup do pole typu number
    vyska = page.locator("#frm-calcForm-BMI_Vyska")

    # Pokusíme se vyplnit "zkouška" do inputu a zachytit výjimku
    try:
        vyska.fill("zkouška")
        pytest.fail("Výjimka nebyla vyvolána při pokusu o vyplnění neplatného vstupu do input[type=number]")
    except Error as e:
        assert "Cannot type text into input[type=number]" in str(e), f"Očekávaná chyba nebyla vyvolána: {e}"

  


    

   




     