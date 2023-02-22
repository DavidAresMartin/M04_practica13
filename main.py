from book import book
from user import user
from university import university
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
