import unittest
from control import Control
from modelo import Modelo

class ControlTest(unittest.TestCase):
    
    def setUp(self):
        control=Control()
        
    def tearDown(self):
        self.control=None
        
    def testMediaNotNull(self):
        self.assertIsNoNone(self.control,"No debe ser nulo")

    def testMediaIncorrecta(self):
        valores= [50,22,18,34]
        self.modelo.assertEqual(self.modelo.getValoreMedio(valores),31,"La media entre los valores anteriores tiene que ser 31")
        

if __name__ == "__main__":
    unittest.main()