import tkinter
from Modelo.PerceptronSimpleAND import PerceptronSimpleAND
from Modelo.Grafico import Grafico
from Vista.Vista import Vista
from Controlador.Controlador import Controlador

ventana = tkinter.Tk()
modelo_inicial = PerceptronSimpleAND()
vista = Vista(ventana)
grafico = Grafico(ventana, modelo_inicial)
controlador = Controlador(vista, grafico, ventana, modelo_inicial)

ventana.mainloop()