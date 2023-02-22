class user:
    # els atributs seran de nom , cognom , la edad el seu genere , el email i el password
    def __init__(self, nom, cognom, edad, genero, email, password,):
        self.nom = nom
        self.cognom = cognom
        self.edad = edad
        self.genero = genero
        self.email = email
        self.password = password

    def getNom(self):
        return self.nom
    def setNom(self, nom):
        self.nom = nom

    def getCognom(self):
        return self.cognom
    def setCognom(self, cognom):
        self.cognom = cognom

    def getEdad(self):
        return set.edad
    def setEdad(self, edad):
        self.edad = edad

    def getGenero(self):
        return self.genero
    def setGenero(self, genero):
        self.genero = genero

    def getEmail(self):
        return self.email
    def setEmail(self, email):
        self.email = email

    def getPassword(self):
        return self.password
    def setPassword(self, password):
        self.password = password

    def salutacio(self):
        print("El teu nom és " +self.nom)
        print("El teu cognom es " +self.cognom)
        print("La teva edad es " +self.edad)
        print("Et identificas com "+self.genero)
        print("Email: " +self.email)
        print("El teu password es" +self.password)