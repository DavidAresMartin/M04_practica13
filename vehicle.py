class Vehicle:
    def __int__(self, placa, tipo, marca, color, model, ocupantes):
        self.placa = placa
        self.tipo = tipo
        self.marca = marca
        self.color = color
        self.model = model
        self.ocupantes = ocupantes


    def parts(self):
        print("La placa del vehicle és: " + self.placa)
        print("El tipus és: " + self.tipo)
        print("La marca és: " + self.marca)
        print("El seu color és" + self.color)
        print("El model  és: " + self.model)
        print("Els ocupants que pot tenir són" + self.ocupantes)




    def getPlaca(self):
        return self.placa

    def setPlaca(self, placa):
        self.placa = placa

    def getTipo(self):
        return self.tipo

    def setTipo(self, tipo):
        self.tipo = tipo

    def getMarca(self):
        return self.marca

    def setMarca(self, marca):
        self.marca = marca

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def getModel(self):
        return self.model

    def setModel(self, model):
         self.model = model

    def getOcupantes(self):
        return self.ocupantes

    def setOcupantes(self, ocupantes):
        self.ocupantes = ocupantes
