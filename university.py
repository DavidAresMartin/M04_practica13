class university:
    #aqui ficare els atributs del nom de la universitat , la seva direccio, el telefon, el seu horari, provincia i el seu codi postal
    def __init__(self, nom, direccio, telefon, horari, provincia, cp):
        self.nom = nom
        self.direccio = direccio
        self.telefon = telefon
        self.horari = horari
        self.provincia = provincia
        self.cp = cp

    def getNom(self):
        return self.nom
    def setNom(self, nom):
        self.nom = nom

    def getDireccio(self):
        return self.direccio
    def setDireccio(self, direccio):
        self.direccio = direccio

    def getTelefon(self):
        return self.telefon
    def setTelefon(self, telefon):
        self.telefon = telefon

    def getHorari(self):
        return self.horari
    def setHorario(self, horari):
        self.horari = horari

    def getProvincia(self):
        return self.provincia
    def setProvincia(self, provincia):
        self.provincia = provincia

    def getCp(self):
        return self.cp
    def setCp(self, cp):
        self.cp = cp

    def info(self):
        print("Nom: " +self.nom)
        print("Direcció:" +self.direccio)
        print("Telefón: " +self.telefon)
        print("Horari: " +self.horari)
        print("Provincia: "+self.provincia)
        print("Codi Postal: "+self.cp)