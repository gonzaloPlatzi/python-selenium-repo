import unittest
from venv import create
from selenium import webdriver

class RegisterNewUser(unittest.TestCase):   
    
    def setUp(self):       
        self.driver = webdriver.Chrome(executable_path= r'C://Users//gonzalo.robledo//OneDrive - Accenture/Desktop/selenium/chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_new_user(self):
        driver=self.driver
        driver.find_element_by_xpath('//*[@id="header"]/div/div[2]/div/a/span[2]').click()
        driver.find_element_by_link_text('Log In').click()

        create_account_btn = driver.find_element_by_xpath('//*[@id="login-form"]/div/div[1]/div[2]/a/span/span')
        self.assertTrue(create_account_btn.is_displayed() and create_account_btn.is_enabled())
        create_account_btn.click()

        #antes de verificar el form, podemos verificar si realmente estamos creando nuestra cuenta, esto lo podemos chequear con distintos metodos y clases
        self.assertEqual('Create New Customer Account', driver.title)

        #vamos a crear una serie de variables para cada selector
        first_name = driver.find_element_by_id('firstname')
        middle_name = driver.find_element_by_id('middlename')
        last_name = driver.find_element_by_id('lastname')
        email_address = driver.find_element_by_id('email_address')
        news_letter_subscription = driver.find_element_by_xpath('//*[@id="form-validate"]/div[1]/ul/li[4]/label')
        password = driver.find_element_by_id('password')
        confirm_password = driver.find_element_by_id('confirmation')
        submit_button = driver.find_element_by_xpath('//*[@id="form-validate"]/div[2]/button')

        #una vez que tenemos los elementos del form para interactuar, ahora tenemos que verificar que esten habilitados
        self.assertTrue(first_name.is_enabled()
        and middle_name.is_enabled()
        and last_name.is_enabled()
        and email_address.is_enabled()
        and news_letter_subscription.is_enabled()
        and password.is_enabled()
        and confirm_password.is_enabled()
        and submit_button.is_enabled()
        )

        #ahora tenemos que enviar datos a cada uno de esos campos, eso lo hacemos a traves del metodo sendkeys()

        first_name.send_keys('Test')
        middle_name.send_keys('Test')
        last_name.send_keys('Test')
        email_address.send_keys('Test@email.com')
        password.send_keys('1234')
        submit_button.click()   #con esto ya automatizamos el registro para crear una cuenta nueva

    
    def tearDown(self):   
        self.driver.implicitly_wait(3)  
        self.driver.close()
if __name__ == "__main__":
    unittest.main(verbosity = 2)