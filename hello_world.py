import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(unittest.TestCase):    #la clase de divide en 3 componentes
    
    @classmethod        #con este decorador podemos ejecutar las pruebas y no se cierren en la ventana
    def setUpClass(cls):        #setUp va a preparar el entorno de la prueba
        cls.driver = webdriver.Chrome(executable_path= r'C://Users//gonzalo.robledo//OneDrive - Accenture/Desktop/selenium/chromedriver.exe')
        driver = cls.driver
        driver.implicitly_wait(10)
    
    def test_hello_world(self):     #aqui realizamos una serie de acciones para que el navegador las automatice
        driver = self.driver
        driver.get('https://www.platzi.com')

    def test_visit_wikipedia(self):
        self.driver.get('https://www.wikipedia.org')


    @classmethod        #esto ayuda a que nuestros test se corran en una sola ventana y no se este cerrando
    def tearDownClass(cls):     #cierre de ventana de navegador
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'hello_world_report'))