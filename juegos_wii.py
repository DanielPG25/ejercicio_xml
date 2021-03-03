from funciones_wii import *

fichero = LeerXml('nintendo_wii.xml')
opcion = Menu()
while opcion < 1 or opcion > 6:
	print("Esa no es una opción válida")
	opcion = Menu()
while opcion != 6:
	if opcion == 1:
		print("Esta es una lista de juegos con una puntuación general mayor a 4.5 de un total de 5.")
		print()
		juegos = Clasificacion(fichero)
		for a in juegos:
			print(a)
		print()
		opcion = Menu()
	if opcion == 2:
		print("Las regiones disponibles son USA, Europe y Japan.")
		print()
		region=input("Elija una región de las anteriores: ")
		print()
		juegos = ContarRegion(region,fichero)
		print(f"La región {region} tiene un total de {juegos} juegos")
		print()
		opcion=Menu()	
		