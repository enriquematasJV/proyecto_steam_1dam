import unittest
from control import Control

class mediaValoresTest(unittest.TestCase):
    
    def setUp(self):
        self control=Control()
        
    def tearDown(self):
        self.control=None
        
    def testMediaNotNull(self):
        self.assertIsNoNone(self.control,"No debe ser nulo")
        

if __name__ == "__main__":
    unittest.main()