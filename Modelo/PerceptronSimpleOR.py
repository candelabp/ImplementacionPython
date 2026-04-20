import random

class PerceptronSimpleOR:
    def __init__(self):
        self.entradas = [
            [1.0, 1.0, 1.0],
            [1.0, 1.0, -1.0],
            [1.0, -1.0, 1.0],
            [1.0, -1.0, -1.0]
        ]
        self.salidas = [0.0] * 4
        self.factor_aprendizaje = 0.6
        self.w0 = random.random()
        self.w1 = random.random()
        self.w2 = random.random()
        self.y = 0.0
        self.error = 0.0
        self.fila = 0
        self.repeticion = 1
        self.bandera = True

        self.salidas[0] = 1.0
        self.salidas[1] = 1.0
        self.salidas[2] = 1.0
        self.salidas[3] = -1.0

    def getEntradas(self, X):
        if self.fila == 4:
            return self.entradas[3][X]
        else:
            return self.entradas[self.fila][X]

    def getSalidas(self, X):
        if X == 4:
            return self.salidas[3]
        else:
            return self.salidas[X]

    def Entrenamiento(self):
        if self.bandera == True:
            print(f"PERCEPTRON OR")
            print(f"Factor de Aprendizaje: {self.factor_aprendizaje}")
            print(f"Umbral: {self.w0}")
            print(f"Peso 1: {self.w1}")
            print(f"Peso 2: {self.w2}")
            print("")
            print(f"ITERACION: {self.repeticion} -------------------------------------")

            while self.fila < 4:
                print(f"y = ({self.w0}*{self.entradas[self.fila][0]}) + ({self.w1}*{self.entradas[self.fila][1]}) + ({self.w2}*{self.entradas[self.fila][2]})")
                self.y = self.w0 * self.entradas[self.fila][0] + self.w1 * self.entradas[self.fila][1] + self.w2 * self.entradas[self.fila][2]

                print(f"y = {self.y}")

                if self.y > 0:
                    self.y = 1
                    print("Como y > 0 entonces")
                else:
                    self.y = -1
                    print("Como y <= 0 entonces")

                print(f"y = {self.y}")
                self.error = self.salidas[self.fila] - self.y
                print(f"Error = {self.error}")

                if self.error == 0.0:
                    print("-----------------------------------------------------------")
                    self.fila += 1
                else:
                    break

            if self.fila == 4:
                print("\n---------------------------------")
                print("| PESOS FINALES\t\t\t|")
                print(f"| Umbral: {self.w0}\t|")
                print(f"| Peso 1: {self.w1}\t|")
                print(f"| Peso 2: {self.w2}\t|")
                print("---------------------------------\n")
                self.bandera = False

    def Aprendizaje(self):
        print("-----------------------------------------------------------")
        print("Recalculamos los Pesos")
        self.w0 = self.w0 + (self.factor_aprendizaje * self.error * self.entradas[self.fila][0])
        self.w1 = self.w1 + (self.factor_aprendizaje * self.error * self.entradas[self.fila][1])
        self.w2 = self.w2 + (self.factor_aprendizaje * self.error * self.entradas[self.fila][2])
        print(f"Nuevo Umbral = {self.w0}\nNuevo Peso 1 = {self.w1}\nNuevo Peso 2 = {self.w2}")
        self.fila = 0
        self.repeticion += 1
        print("\n")

    def PruebaFuncionamiento(self, entrada1, entrada2):
        y = (self.w0 * 1) + (self.w1 * entrada1) + (self.w2 * entrada2)
        return 1 if y > 0 else -1