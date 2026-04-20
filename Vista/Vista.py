import tkinter
from tkinter import ttk

class Vista:

    def __init__(self, ventana):

        self.ventana = ventana

        ventana.geometry("900x700")
        ventana.title("PERCEPTRON SIMPLE - AND")

        fuenteTitulos = ("Helvetica", 10, "bold")
        estilo = ttk.Style()
        estilo.configure('EstiloBoton.TButton', borderwidth=0, relief="flat", font=("Helvetica", 10, "bold"))
        self.lblSelector = tkinter.Label(ventana, text="Seleccione Operación:", font=fuenteTitulos)
        self.lblSelector.grid(row=0, column=1)

        self.comboModelo = ttk.Combobox(ventana, values=["AND", "OR"], state="readonly", width=10)
        self.comboModelo.set("AND")  
        self.comboModelo.grid(row=0, column=2)

        self.lblTituloPrincipal = tkinter.Label(ventana, text = "HAGA CLICK EN 'Entrenamiento' PARA COMENZAR", font = fuenteTitulos, pady = 10)
        self.lblEntrada1 = tkinter.Label(ventana, text = "Entrada 1:", pady = 10, padx = 90)
        self.lblEntrada2 = tkinter.Label(ventana, text = "Entrada 2:")
        lblEntrada0 = tkinter.Label(ventana, text = "Entrada 0: 1")
        self.lblPeso1 = tkinter.Label(ventana, text = "Peso 1:", pady = 10)
        self.lblPeso2 = tkinter.Label(ventana, text = "Peso 2:")
        self.lblUmbral = tkinter.Label(ventana, text = "Umbral:")
        self.lblSalidaDeseada = tkinter.Label(ventana, text = "Salida Deseada:", pady = 10)
        self.lblSalidaObtenida = tkinter.Label(ventana, text = "Salida Obtenida:")
        self.lblFactorAprendizaje = tkinter.Label(ventana, text = "Factor Aprendizaje: 0.6")
        lblTituloPrueba = tkinter.Label(ventana, text = "EJERCICIO PARA PROBAR EL PERCEPTRON:", font = fuenteTitulos, pady = 10)
        lblPruebaEntrada1 = tkinter.Label(ventana, text = "Entrada 1:", pady = 10)
        lblPruebaEntrada2 = tkinter.Label(ventana, text = "Entrada 2:")
        self.lblPruebaSalidaObtenida = tkinter.Label(ventana, text = "Salida Obtenida:", pady = 10)
        lblR1 = tkinter.Label(ventana, text = "", padx = 15)
        lblR2 = tkinter.Label(ventana, text = "", padx = 15)
        lblR3 = tkinter.Label(ventana, text = "", padx = 15)

        self.btnEntrenamiento = ttk.Button(ventana, text = "Entrenamiento", style='EstiloBoton.TButton', width = 15)
        self.btnAprendizaje = ttk.Button(ventana, text = "Aprendizaje", style='EstiloBoton.TButton', width = 15)
        self.btnPrueba = ttk.Button(ventana, text = "Prueba", style='EstiloBoton.TButton', width = 15)

        self.jtfEntrada1 = tkinter.Entry(ventana)
        self.jtfEntrada2 = tkinter.Entry(ventana)

        self.lblTituloPrincipal.grid(row = 0, column = 3)
        self.lblEntrada1.grid(row = 1, column = 2)
        self.lblEntrada2.grid(row = 1, column = 3)
        lblEntrada0.grid(row = 1, column = 4)
        self.lblPeso1.grid(row = 2, column = 2)
        self.lblPeso2.grid(row = 2, column = 3)
        self.lblUmbral.grid(row = 2, column = 4)
        self.lblSalidaDeseada.grid(row = 3, column = 2)
        self.lblSalidaObtenida.grid(row = 3, column = 3)
        self.lblFactorAprendizaje.grid(row = 3, column = 4)
        lblTituloPrueba.grid(row = 4, column = 3)
        lblPruebaEntrada1.grid(row = 5, column = 2)
        lblPruebaEntrada2.grid(row = 5, column = 3)
        self.lblPruebaSalidaObtenida.grid(row = 6, column = 4)
        lblR1.grid(row = 1, column = 0)
        lblR2.grid(row = 3, column = 0)
        lblR3.grid(row = 5, column = 0)

        self.btnEntrenamiento.grid(row = 1, column = 1)
        self.btnAprendizaje.grid(row = 3, column = 1)
        self.btnPrueba.grid(row = 5, column = 1)

        self.jtfEntrada1.grid(row = 6, column = 2)
        self.jtfEntrada2.grid(row = 6, column = 3)
