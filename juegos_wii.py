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
		while opcion < 1 or opcion > 6:
			print("Esa no es una opción válida")
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
		while opcion < 1 or opcion > 6:
			print("Esa no es una opción válida")
			opcion = Menu()	
	if opcion == 3:
		print("Ahora buscaremos los juegos que empiecen por la cadena introducida a continuación")
		cadena = input("Dime la cadena (empiece por mayúscula): ")
		juegosa = BuscarPorCadena(cadena,fichero)
		print()
		for a in juegosa:
			print(f"El juego {a.get('nombre')[0]} fue desarrollado por {a.get('desarrolladora')[0]} en el año {a.get('año')[0]}.")
		print()
		opcion=Menu()
		while opcion < 1 or opcion > 6:
			print("Esa no es una opción válida")
			opcion = Menu()
	if opcion == 4:
		print("Ahora buscaremos juegos a partir de su género.")
		print("Esta es una lista de los genéros más importantes para poder buscar:")
		print("Action, Shooter, Driving, Party, Adventure, Puzzle, Fitness, Rhythm, Board Game, Tennis, Hockey, Golf, Role-Playing, Simulation, Fishing, Flying, Quiz, Platform, Soccer, Football, etc")
		genero = input("Elige uno de los géneros anteriores: ")
		juegosb = BuscarPorGenero(genero,fichero)
		print()
		print(f"Los juegos del género {genero} son:")
		print()
		for a in juegosb:
			print(a[0])
		print()
		opcion=Menu()
		while opcion < 1 or opcion > 6:
			print("Esa no es una opción válida")
			opcion = Menu()
	if opcion == 5:
		jugadores=int(input("Introduce el número de jugadores (máximo 12): "))
		juegosc=BuscarPorJugadores(jugadores,fichero)
		print()
		print("Las clasificaciones por edad son las siguientes:")
		print("Everyone, E10+, Teen, Kids to Adults, Mature")
		print()
		edad = input("Elige una de las anteriores (tal y como están escritas arriba): ")
		print()
		print("Si la búsqueda por clasificación de edad está vacía, es que no hay ningún juego con esa clasificación para los jugadores que ha pedido.")
		print()
		juegosfiltrados = FiltrarPorEdad(edad,juegosc)
		print()
		print("Los juegos con esa clasificacion por edad son: ")
		for a in juegosfiltrados:
			print(a)
		opcion=Menu()
		while opcion < 1 or opcion > 6:
			print("Esa no es una opción válida")
			opcion = Menu()
print("Programa finalizado")						
		