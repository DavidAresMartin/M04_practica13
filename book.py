class book:
    #de un llibre ficare els atributs de titol autor, genere ,data que es va publicar,las paginas que conte i el seu isbn
    def __init__(self, titol, autor, genero, data, paginas, isbn ):
        self.titol = titol
        self.autor = autor
        self.genero = genero
        self.data = data
        self.paginas = paginas
        self.isbn = isbn

    def getTitol(self):
        return self.titol
    def setTitol(self, titol):
        self.titol = titol

    def getAutor(self):
        return self.autor
    def setAutor(self, autor):
        self.autor = autor

    def getGenero(self):
        return self.genero
    def setGenero(self, genero):
        self.genero = genero

    def getData(self):
        return self.data
    def setData(self, data):
        self.data = data

    def getPaginas(self):
        return self.paginas
    def setPaginas(self, paginas):
        self.paginas = paginas

    def getISBN(self):
        return self.isbn
    def setISBN(self, isbn):
        self.isbn = isbn



    def info(self):
        print("El titol del llibre es "+ self.titol)
        print("El autor del llibre es " + self.autor)
        print("El genere del llibre es " +self.genero)
        print("La data que se va publicar va ser el " +self.data)
        print("El llibre té "+self.paginas + " paginas")
        print("El ISBN del llibre es " +self.isbn)