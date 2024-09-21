import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def api_context():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        yield context.request  
        browser.close()

def test_get_user(api_context):
    # Provedeme GET požadavek na uživatele s ID 1
    response = api_context.get('https://jsonplaceholder.typicode.com/users/1')
    
    # Ověříme, že odpověď byla úspěšná (status kód 200)
    assert response.status == 200, f"Chybný status kód: {response.status}"
    
    # Ověříme, že obsah odpovědi je správný
    user = response.json()  
    assert user["id"] == 1
    assert user["name"] == "Leanne Graham"  # Ověření správného jména uživatele


def test_create_post(api_context):
    # Data, která budeme posílat
    new_post_data = {
        "title": "Testovací příspěvek",
        "body": "Toto je obsah testovacího příspěvku",
        "userId": 1
    }

    # Odeslání POST požadavku s daty
    response = api_context.post('https://jsonplaceholder.typicode.com/posts', data=new_post_data)
    
    # Ověření, že odpověď byla úspěšná (status kód 201 značí úspěšné vytvoření)
    assert response.status == 201, f"Chybný status kód: {response.status}"
    
    # Ověření, že odpověď obsahuje správná data
    created_post = response.json()
    assert created_post["title"] == new_post_data["title"]
    assert created_post["body"] == new_post_data["body"]
    assert created_post["userId"] == new_post_data["userId"]
    
    # Ověření, že nově vytvořený záznam má ID (které přiděluje server)
    assert "id" in created_post, "ID nově vytvořeného příspěvku chybí"
    print(f"Nově vytvořený příspěvek má ID: {created_post['id']}")

