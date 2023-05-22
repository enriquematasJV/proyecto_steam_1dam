from sense_emu import SenseHat

class Mediciones:

    def __init__(self):
        self.sense=SenseHat()
    
        self.temperaturas=[]
        self.presiones=[]
       
   
   
   
    def get_temperatura(self):
        t=round(self.sense.temp, 2)
        self.temperaturas.append(t)
        return t       
        
     
    def get_temperaturas(self):
         return self.temperaturas
  
    def get_presion(self):
        p=self.sense.get_pressure()
        self.presiones.append(p)
        return p

    def get_presiones(self):
        return self.presiones
    def get_valor_medio(self,lista):
       pass
    
    def get_valor_max(self,lista):
       pass
    
    def get_valor_min(self,lista):
       pass    
                                            
        


                
        
        