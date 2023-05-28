import unittest
from modelo import Modelo

class ModeloTest(unittest.TestCase):

    def setUp(self):
        self.modelo = Modelo()

    def testHumedadNoMenorQueCero(self):
        humedad = self.modelo.getHumedad()
        
        self.assertGreaterEqual(humedad, 0, "La humedad no debe ser menor que cero")
        print("Humedad menor que 0")

    def testHumedadNoMayorQueCien(self):
        humedad = self.modelo.getHumedad()

        # Verificamos que la humedad no sea mayor que cien
        self.assertLessEqual(humedad, 100, "La humedad no debe ser mayor que cien")
        print("Humedad mayor que 100")
        
    if __name__ == '__main__':
        unittest.main()