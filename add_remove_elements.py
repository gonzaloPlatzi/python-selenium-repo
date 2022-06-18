from lib2to3.pgen2 import driver
from time import sleep
import unittest
from requests import delete
from selenium import webdriver
#from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class AddRemoveElements(unittest.TestCase):   
    
    def setUp(self):       
        self.driver = webdriver.Chrome(executable_path= r'C://Users//gonzalo.robledo//OneDrive - Accenture/Desktop/selenium/chromedriver.exe')
        driver = self.driver
        driver.maximize_window()
        driver.get('https://the-internet.herokuapp.com/')
        driver.find_element_by_link_text('Add/Remove Elements').click()

    def test_add_remove(self):
        driver = self.driver

        elements_added = int(input('How many elements will you ADD?: '))
        elements_removed = int(input('How many elements will you REMOVE?: '))
        total_elements = elements_added - elements_removed

        add_button = driver.find_element_by_xpath('//*[@id="content"]/div/button')
        sleep(3)

        for i in range(elements_added):
            add_button.click()
        
        #si queire eliminar mas elemento de lo que existe, no continuara el script, para eso es nuestro try-catch
        for i in range(elements_removed):
            try:
                delete_button = driver.find_element_by_xpath('//*[@id="elements"]/button[1]')
                delete_button.click()
            except:
                print("You're trying to delete more elements than the existent")
                break
            #mostramos en consola que paso al final
        if total_elements > 0:
            print(f"There are {total_elements} elements on screen")
        else:
            print("There are 0 elements on screen")
        
        sleep(3)

    def tearDown(self):   
        self.driver.implicitly_wait(3)  
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity = 2)