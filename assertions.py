from ast import Try
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException   #nos servira como excepcion para nuestros assertions
from selenium.webdriver.common.by import By

class AssertionsTest(unittest.TestCase):

    def setUp(self):       
        self.driver = webdriver.Chrome(executable_path= r'C://Users//gonzalo.robledo//OneDrive - Accenture/Desktop/selenium/chromedriver.exe')
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(15)
        driver.get('http://demo-store.seleniumacademy.com/')

    #metodos para nuestros assertions
    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME, 'q'))

    def test_language_option(self):
        self.assertTrue(self.is_element_present(By.ID, 'select-language'))
   
    def test_search_text_field(self):
        search_field = self.driver.find_element_by_id('search')
    
    def tearDown(self):     
        self.driver.quit()
    
    def is_element_present(self, how, what):    #esta funcion va a servirnos para identifcar cuando un elemento esta presente de acuerdo a sus parametros, how el tipo de selector y what el valor que tiene
        try:
            self.driver.find_element(by = how, value = what)
        except NoSuchElementException as variable:
            return False
        return True
        

if __name__ == "__main__":
    unittest.main(verbosity = 2)
        