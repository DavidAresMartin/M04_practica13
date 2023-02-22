class School:
    def __int__(self, alumnos, profesores, materias, clases, hora_entrada, hora_salida):
        self.alumnos = alumnos
        self.profesores = profesores
        self.materias = materias
        self.clases = clases
        self.hora_entrada = hora_entrada
        self.hora_salida = hora_salida


    def info(self):
        print("Hi ha  " + self.alumnos + "alumnes a l'escola")
        print("Hi ha  " + self.profesores + "profesors a l'escola")
        print("Hi ha " + self.materias + "materias en l'escola")
        print("Hi ha " + self.clases + "clases en l'escola")
        print("L'hora d'entrada de l'escola es a les  " + self.hora_entrada)
        print("L'hora de salida de l'escola es a les " + self.hora_salida)




    def getAlumnos(self):
        return self.alumnos

    def setAlumnos(self, alumnos):
        self.alumnos = alumnos

    def getProfesores(self):
        return self.profesores

    def setProfesores(self, profesores):
        self.profesores = profesores

    def getMaterias(self):
        return self.materias

    def setMaterias(self, materias):
        self.materias = materias

    def getClases(self):
        return self.color

    def setClases(self, clases):
        self.clases = clases

    def getHora_entrada(self):
        return self.hora_entrada

    def setHora_entrada(self, hora_entrada):
         self.hora_entrada = hora_entrada

    def getHora_salida(self):
        return self.hora_salida

    def setHora_salida(self, hora_salida):
        self.hora_salida = hora_salida
