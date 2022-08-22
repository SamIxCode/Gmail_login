Vypracované zadanie automatického prihlasovanie do G-mail.

Kedže Google rozpozná že sa jedná o automatizované prihlásenie, ako driver som použil undetected-chromedriver.

Niektoré časti kódu ako napríklad WebDriverAwait na samom konci, kde čáká kýmneuvidí element webu po odhlásení, je tak napísaní pretože v undetected-chromedriver nie je možné nastaviť "experimental_option("detach", True)"
