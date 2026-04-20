from tkinter import messagebox
import matplotlib.pyplot as plt
from Modelo.PerceptronSimpleAND import PerceptronSimpleAND
from Modelo.PerceptronSimpleOR import PerceptronSimpleOR


class Controlador:
    def __init__(self, Vista, Grafico, Ventana, modelo):
        self.vista, self.grafico, self.ventana, self.modelo = Vista, Grafico, Ventana, modelo

        self.vista.btnEntrenamiento.config(command=self.EventEntrenamiento)
        self.vista.btnAprendizaje.config(command=self.EventAprendizaje)
        self.vista.btnPrueba.config(command=self.EventPrueba)
        self.vista.comboModelo.bind("<<ComboboxSelected>>", self.CambiarModelo)
        self.grafico.canvas.mpl_connect('close_event', lambda e: plt.close())

    def CambiarModelo(self, event):
        seleccion = self.vista.comboModelo.get()
        self.modelo = PerceptronSimpleAND() if seleccion == "AND" else PerceptronSimpleOR()
        self.vista.ventana.title(f"PERCEPTRON SIMPLE - {seleccion}")
        self.grafico.modelo = self.modelo
        self.grafico.DibujarEjes()
        messagebox.showinfo("Reinicio", f"Modelo cambiado a {seleccion}. Pesos reseteados.")

    def EventEntrenamiento(self):
        self.modelo.Entrenamiento()
        self.vista.lblTituloPrincipal.config(text="COMPLETADO" if not self.modelo.bandera else "FALLIDO")
        self.vista.lblEntrada1.config(text=f"Entrada 1: {self.modelo.getEntradas(1)}")
        self.vista.lblEntrada2.config(text=f"Entrada 2: {self.modelo.getEntradas(2)}")
        self.vista.lblPeso1.config(text=f"Peso 1: {round(self.modelo.w1, 4)}")
        self.vista.lblPeso2.config(text=f"Peso 2: {round(self.modelo.w2, 4)}")
        self.vista.lblUmbral.config(text=f"Umbral: {round(self.modelo.w0, 4)}")
        self.vista.lblSalidaDeseada.config(text=f"Deseada: {self.modelo.getSalidas(self.modelo.fila)}")
        self.vista.lblSalidaObtenida.config(text=f"Obtenida: {self.modelo.y}")

        try:
            x1, x2 = -2, 2
            y1 = (-self.modelo.w0 - self.modelo.w1 * x1) / self.modelo.w2
            y2 = (-self.modelo.w0 - self.modelo.w1 * x2) / self.modelo.w2
            self.grafico.GraficarRecta(x1, x2, y1, y2, self.modelo.repeticion)
        except ZeroDivisionError:
            pass

    def EventAprendizaje(self):
        if self.modelo.error != 0.0:
            self.modelo.Aprendizaje()
            messagebox.showinfo("Pesos", "Pesos recalculados.")

    def EventPrueba(self):
        try:
            res = self.modelo.PruebaFuncionamiento(int(self.vista.jtfEntrada1.get()), int(self.vista.jtfEntrada2.get()))
            self.vista.lblPruebaSalidaObtenida.config(text=f"Salida: {res}")
        except:
            messagebox.showerror("Error", "Use 1 o -1")