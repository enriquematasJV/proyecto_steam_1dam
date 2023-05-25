from sense_emu import SenseHat

class Mediciones:
    

    def __init__(self):
        self.sense=SenseHat()
    
        self.temperaturas=[]
        
        self.presiones=[]
        
        self.humedades=[]
       
   
   
   
    def get_temperatura(self):
        t=round(self.sense.temp, 2)
        self.temperaturas.append(t)
        return t       
        
     
    def get_temperaturas(self):
         return self.temperaturas
        
    def get_humedades(self):
         return self.humedades
        
    def get_presiones(self):
         return self.presiones
  
        
    
    def get_valor_medio(self,lista):
        pass
    
    def get_valor_max(self,lista):
        valor_max = max(lista)
        return valor_max
            
    
    def get_valor_min(self,lista):
        valor_min = min(lista)
        return valor_min   
                                            
        
    def leer_fichero():
        f = open("./Datos.txt")
        return f