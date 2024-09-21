1. 1.test/test_navi.py
   Použit pouze pro ověření, že mi testovací prostředí funguje

2. 2.test/test.click.py
   test_navi - Ověřuje titulek a nadpis stránky
   test_click - Ověřuje tlačitko na přesměrování na stránku s kurzy

3) 3.test/test.calc.py
   test_bmi - Testuje funkčnost BMI kalkulačky pro platné vstupy (165 cm a 58 kg), ověřuje správnost výpočtu BMI.
   test_invalid_bmi_input - Testuje chování BMI kalkulačky při neplatném vstupu (text místo čísla) a očekává, že dojde k chybě.

4) 4.test/test_api.py
   test_get_user - Ověřuje správné načtení uživatele s ID 1 z API. Kontroluje status kód 200 a správné informace o uživateli.
   test_create_post - Simuluje vytvoření nového příspěvku pomocí POST požadavku. Ověřuje status kód 201 (úspěšné vytvoření) a kontroluje, zda nově vytvořený příspěvek obsahuje stejná data jako požadavek.
