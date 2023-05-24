from modelo import Mediciones
from vista import Vista


class Control:
    
    def __init__(self):
        
        self.vista=Vista()
        self.modelo=Mediciones()
        
   
    def inicio(self):
        
        opcion="0"
                         
        while opcion!="s":
    
            if opcion == "0":
               opcion=self.vista.menu()
            elif opcion == "1":
               t=self.modelo.get_temperatura()
               self.vista.mostrar_temperatura(t)
               opcion="0"
            elif opcion == "4":
               self.vista.mostrar_grafico_temperatura(self.modelo.get_temperaturas())
               opcion="0" 
            elif opcion == "10":
               m = self.modelo.get_valor_max(self.modelo.get_temperaturas())
               self.vista.mostrar_valor_max(m,"temperatura")
               opcion="0"
            elif opcion == "11":
               m = self.modelo.get_valor_max(self.modelo.get_presiones())
               self.vista.mostrar_valor_max(m,"presion")
               opcion="0"
            elif opcion == "12":
               m = self.modelo.get_valor_max(self.modelo.get_humedades())
               self.vista.mostrar_valor_max(m,"humedad")
               opcion="0"
            
            elif opcion == "13":
               m = self.modelo.get_valor_min(self.modelo.get_temperaturas())
               self.vista.mostrar_valor_min(m,"temperatura")
               opcion="0"
            elif opcion == "14":
               m = self.modelo.get_valor_min(self.modelo.get_presiones())
               self.vista.mostrar_valor_min(m,"presion")
               opcion="0"
            elif opcion == "15":
               m = self.modelo.get_valor_min(self.modelo.get_humedades())
               self.vista.mostrar_valor_min(m,"humedad")
               opcion="0"
           
            elif opcion == "s":
               print("¡Hasta luego!")
               break
            else:
               opcion=self.vista.menu

        