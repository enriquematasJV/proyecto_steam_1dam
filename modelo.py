from sense_emu import SenseHat

class Mediciones:

    def __init__(self):
        self.sense=SenseHat()
    
        self.temperaturas=[]
      
        self.presiones=[]
       
        self.humedades=[]

       
    def get_humedad(self):
       h=round(self.sense.humidity,2)
       self.humedades.append(h)
       return h
      
    def get_presion(self):
        p = round(self.sense.get_pressure(),0)
        self.presiones.append(p)
        return p
   
   
    def get_temperatura(self):
        t=round(self.sense.temp, 2)
        self.temperaturas.append(t)
        return t       
        
     
    def get_temperaturas(self):
         return self.temperaturas
   

    def get_presiones(self):
        return self.presiones

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
        valor_max = max(lista)
        return valor_max
            
    
    def get_valor_min(self,lista):
        valor_min = min(lista)
        return valor_min   
                                            
        
    def leer_fichero():
        f = open("./Datos.txt")
        return f                        
        

    def escribir(self,listHmd,listPr,listTemp):
       file= open('Datos.txt','a')
       file.write("Humedad: \n")
       for i in listHmd:
           file.write(i+'\n')
       file.write("Presion: \n")
       for i in listPr:
           file.write(i+'\n')
       file.write("Temperatura: \n")
       for i in listTemp:
           file.write(i+'\n')
       
       file.close()

    def medir_temperatura_constante(self):
        while True:
            temp = self.sense.temp
            print(temp)
            pixels = [self.red if i < temp else self.blue for i in range(64)]
            self.sense.set_pixels(pixels)
