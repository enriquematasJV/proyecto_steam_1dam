from sense_emu import SenseHat
import pandas as pd
import matplotlib.pyplot as plt

class Vista:
    
    def __init__(self):
        self.sense=SenseHat()
        
    def menu(self):
        print("0. Menú:")
        print("1. Medir temperatura")
        print("2. Medir presión")
        print("3. Medir humedad")
        print("4. Grafico de la temperatura")
        print("5. Grafico de la presion")
        print("6. Grafico de la humedad")
        print("7. Valor medio de la temperatura")
        print("8. Valor medio de la presión")
        print("9. Valor medio de la humedad")
        print("s. Salir")
        return input("Ingrese la opción deseada: ")
    
    def mostrar_temperatura(self,t):
        self.sense.show_message("{}C".format(t))
        print(t)

    def mostrar_presion(self,p):
        self.sense.show_message("{}Mbar".format(p))
        print(p)
    
    def mostrar_valor_medio(self, m, texto):
       pass
    
    
    def mostrar_grafico_temperatura (self, temperaturas):
        df_temperatura = pd.DataFrame({'Temperatura': temperaturas})

        # crear un gráfico de línea
        df_temperatura.plot(kind='line')

        # personalizar el gráfico con títulos y etiquetas de los ejes
        plt.title('Temperatura')
        plt.xlabel('Tiempo (minutos)')
        plt.ylabel('Temperatura (°C)')

        # mostrar el gráfico
        plt.show()
        
   
            
