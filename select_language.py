#Manejo de dropdowns y listas
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select


class LanguageOptions(unittest.TestCase):   
    
    def setUp(self):       
        self.driver = webdriver.Chrome(executable_path= r'C://Users//gonzalo.robledo//OneDrive - Accenture/Desktop/selenium/chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(15)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_select_language(self):
        #para manipular dropdowns importamos el modulo Select de selenium, asi podremos elegir cada opcion del dropdown
        #creamos una lista
        exposed_options = ['English', 'French', 'German']

        #creamos una nueva lista pero vacia para almacenar las opciones que elijamos cuando las esetemos revisando
        actual_options = []

        #para acceder a las opciones del drowdown
        select_language = Select(self.driver.find_element_by_id('select-language'))

        #validamos que tengamos tres opciones
        self.assertEqual(3, len(select_language.options))   #comparamos las opciones, nos permite ingresar a las opciones del dropdown

        #iteramos por cada una de las opciones
        for option in select_language.options:
            actual_options.append(option.text)

        #revisa que la lista de las opciones activar y expuestas sean identicas
        self.assertListEqual(exposed_options, actual_options)

        self.assertEqual('English', select_language.first_selected_option.text) #verificamos que la palabra English sea la primera seleccionada de nuestro dropwdown

        select_language.select_by_visible_text('German')

        self.assertTrue('store=german' in self.driver.current_url)

        select_language = Select(self.driver.find_element_by_id('select-language'))
        select_language.select_by_index(0)  #sellecionamos ingles para el valor 0
    
    def tearDown(self):   
        self.driver.implicitly_wait(3)  
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity = 2)