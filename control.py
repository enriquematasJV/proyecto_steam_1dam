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
            elif opcion =="7":
                t=self.modelo.get_valor_medio(self.modelo.get_temperaturas())
                self.vista.mostrar_valor_medio(t,"temperatura")
                opcion="0"
            elif opcion =="8":
                p=self.modelo.get_valor_medio(self.modelo.get_presion())
                self.vista.mostrar_valor_medio(p,"presion")
                opcion="0"
            elif opcion =="9":
                h=self.modelo.get_valor_medio(self.modelo.get_humedad())
                self.vista.mostrar_valor_medio(h,"humedad")
                opcion="0"
            elif opcion =="10":
                self.modelo.escribir(self.modelo.get_humedades(),self.modelo.get_presiones(),self.modelo.get_temperaturas())
                opcion="0"
            elif opcion == "s":
               print("¡Hasta luego!")
               break
            else:
               opcion=self.vista.menu()

        