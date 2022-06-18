#Demoras
#Implicita: una demora implicita busca un elemento en el DOM y en el caso de que lo encuentre va a continuar, para ello va a esperar una cantidad de tiempo
#determinado y estas pausas ya las hemos utilizado
#Explicita: esperan a que se cumpla una condicion determinada de acuerdo a un set de condiciones que ya existen, nos ayudan a que primero se encuentre esa condicion se cumpla yd espues selenium pueda continuar
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By #By nos ayuda a hacer refencia a un elemento del sitio web a traves de sus selectores, no para identificarlo si no para interactuar distinto a como lo hace driver
from selenium.webdriver.support.ui import WebDriverWait #nos permitira hacer uno de las expected conditions
from selenium.webdriver.support import expected_conditions as EC

class ExplicitWaitTests(unittest.TestCase):   
    
    def setUp(self):       
        self.driver = webdriver.Chrome(executable_path= r'C://Users//gonzalo.robledo//OneDrive - Accenture/Desktop/selenium/chromedriver.exe')
        driver = self.driver
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_account_link(self):
        #hace referencia a webdriver y esperar 10 segundos
        WebDriverWait(self.driver, 10).until(lambda s: s.find_element_by_id('select-language').get_attribute('length') == '3')

        account = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'ACCOUNT')))
        account.click()


    def test_create_new_customer(self):
        self.driver.find_element_by_link_text('ACCOUNT').click()

        my_account = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'My Account')))
        my_account.click()

        create_account_btn = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, 'CREATE AN ACCOUNT')))
        create_account_btn.click()

        WebDriverWait(self.driver, 10).until(EC.title_contains('Create New Customer Account'))
   
    def tearDown(self):   
        self.driver.implicitly_wait(3)  
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity = 2)