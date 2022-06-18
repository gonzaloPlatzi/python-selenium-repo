from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from assertions import AssertionsTest
from searchtests import SearchTests

#con las variables cargamos los casos de prueba
assertions_test = TestLoader().loadTestsFromTestCase(AssertionsTest)
search_test = TestLoader().loadTestsFromTestCase(SearchTests)

#el siguiente paso es construir la suite de prueba a traces del codigo, le pasamos por parametro la lista de las variables donde cargamos las pruebas
smoke_test = TestSuite([assertions_test, search_test])

#lo siguiente es indicar los parametros para generar el reporte, mediante un diccionario
kwargs = {
    "output": 'smoke-report'
}

#aqui pasaremos el test runner con los argumentos para que se genere el reporte de la forma que deseamos
runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)