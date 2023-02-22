from book import book
from user import user
from university import university
from animal import Animal
from school import School
from vehicle import Vehicle
#cambio el nombre de autor
b1 = book("Aventuras", "Elihú Valdelomar", "aventura", "11-04-2010", "342" , "ISBN 0-5645-2621-3")
b1.info()
b1.setAutor("Roger Sobrino")
b1.info()
#cambio la edad
u1 = user("Elihú", "Valdelomar", "80", "Masculino", "evaldelo22@jaumebalmes.net", "1234")
u1.salutacio()
u1.setEdad("18")
u1.salutacio()
#cambio de provincia
uni = university("Universidad de Barcelona", " Gran Via de les Corts Catalanes, 585", "612345678", "7:00-21:00", "Girona", "08007")
uni.info()
uni.setProvincia("Barcelona")
uni.info()

#cambio de animal
a1 = Animal("Lleo", "Feliu", "Carnivor", "12", "marro groguenc", "15")
a1.salutacio()
a1.setNombre("Gat")
a1.salutacio()

#cambio de alumnos
s1 = School("120", "25", "15", "35", " 8:00", "2:35")
s1.info()
s1.setAlumnos("100")
s1.info()

#cambio de color
c1 = Vehicle("f1 1929", "Ferrari", "GTS", "vermell", "ferrari 296 GTB", 2)
c1.parts()
c1.setColor("verd")
c1.parts()
