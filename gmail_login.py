
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from getpass import getpass

class main:
    def __init__(self) -> None:
            self.url    = 'https://accounts.google.com/ServiceLogin'
            self.driver = uc.Chrome(use_subprocess=True)
            self.time   = 10
            

    def log_in (self, email, password):

        self.driver.get(self.url)

        #odosať prihlasovacie údaje(email)
        WebDriverWait(self.driver, 1000).until(EC.visibility_of_element_located((By.ID, 'identifierId'))).send_keys(f'{email}')
        self.driver.find_element(By.ID,"identifierNext").click()

        #odosať prihlasovacie údaje(password)
        WebDriverWait(self.driver, 1000).until(EC.visibility_of_element_located((By.NAME, 'password'))).send_keys(f'{password}')
        self.driver.find_element(By.ID,"passwordNext").click() 

        #ak je aktivované dvojstupňové overenie
        if self.driver.find_element(By.ID,'headingSubtext').is_displayed() == True:
            print('dokončite overenie totožnosti na mobilnom zariadení')

        

        
    def gmail_inbox(self):
        self.log_in(email,password)
        WebDriverWait(self.driver, 1000).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/c-wiz/c-wiz/div/div[3]/div/div/header/div[2]/a')))
        print('succesfully logged in')
        self.driver.get('https://mail.google.com/mail/u/0/#inbox') 
        WebDriverWait(self.driver, 99999).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="headingText"]/span')))
        #okno ostane otvorné kým sa neodhásite

if __name__ == '__main__':
    email=input('zadajte emailovú adresu:  ')
    password= getpass('Zadajte heslo:  ')
    print(f'email:{email}')
    driver=main()
    driver.gmail_inbox()
