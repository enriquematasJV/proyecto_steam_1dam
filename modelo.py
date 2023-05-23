from sense_emu import SenseHat

class Mediciones:

    def __init__(self):
        self.sense=SenseHat()
    
        self.temperaturas=[]
       
        self.presion=[]
       
        self.humedad=[]
   
   
    def get_temperatura(self):
        t=round(self.sense.temp, 2)
        self.temperaturas.append(t)
        return t       
        
     
    def get_temperaturas(self):
         return self.temperaturas
    
    def get_presion(self):
         return self.presion

    def get_humedad(self):
         return self.humedad
    
    def get_valor_medio(self,lista):
        suma=0
        cont=0
        for i in lista :
            suma=i+suma
            cont=cont+1
        
        result=suma/cont
        result=round(result,2)
        return result
    
    def get_valor_max(self,lista):
       pass
    
    def get_valor_min(self,lista):
       pass    
                                            
        


                
        
        