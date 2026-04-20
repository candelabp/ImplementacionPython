from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


class Grafico:

    def __init__(self, Ventana, modelo):
        self.ventana = Ventana
        self.modelo = modelo

        # Creamos la figura y el canvas UNA SOLA VEZ
        self.figura = Figure(figsize=(5, 4), dpi=100)
        self.subgrafico = self.figura.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(self.figura, master=self.ventana)
        self.canvas.get_tk_widget().grid(row=7, column=2, columnspan=5)

        # Dibujamos el estado inicial
        self.DibujarEjes()

    def DibujarEjes(self):
        self.subgrafico.clear()
        self.subgrafico.grid(True)
        self.subgrafico.set_xlim(-2, 2)
        self.subgrafico.set_ylim(-2, 2)

        self.subgrafico.spines['left'].set_position('zero')
        self.subgrafico.spines['bottom'].set_position('zero')
        self.subgrafico.spines['right'].set_color('none')
        self.subgrafico.spines['top'].set_color('none')

        # Dibujamos los puntos dinámicamente según el modelo (AND u OR)
        # entradas[i][1] es X, entradas[i][2] es Y
        for i in range(4):
            x_punto = self.modelo.entradas[i][1]
            y_punto = self.modelo.entradas[i][2]
            salida = self.modelo.salidas[i]

            # Si la salida es 1 pintamos verde, si es -1 pintamos rojo
            color = 'go' if salida == 1.0 else 'ro'
            self.subgrafico.plot(x_punto, y_punto, color)

    def GraficarRecta(self, x1, x2, y1, y2, repeticion):
        # Limpiamos y redibujamos puntos y ejes
        self.DibujarEjes()

        # Dibujamos la nueva recta
        x = [x1, x2]
        y = [y1, y2]
        self.subgrafico.plot(x, y, color='purple', linestyle='--', label=f"Iteración: {repeticion}")

        self.subgrafico.legend(loc='upper right')

        # En lugar de crear un canvas nuevo, solo refrescamos el existente
        self.canvas.draw()