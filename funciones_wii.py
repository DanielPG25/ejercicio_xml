from lxml import etree
import sys

def LeerXml(fichero):
	fichero = etree.parse(fichero)
	return fichero

def Menu():
	print("1. Mejores juegos para la Wii (según su clasificación)")
	print("2. Juegos por región")
	print("3. Buscar por nombre")
	print("4. Buscar por género")
	print("5. Buscar por número de jugadores y edad recomendada")
	print("6. Salir")
	opcion = int(input("Dime que opción eliges: "))
	return opcion

def Clasificacion(fichero):
	lista = fichero.xpath("//menu/game[score>=4.5]/description/text()")
	return lista

def ContarRegion(region,fichero):
	lista=[]
	lista2 = fichero.xpath("/menu/game")
	for a in lista2:
		if region in a.xpath("./@name")[0]:
			lista.append(a.xpath("./description/text()"))
	return len(lista)

def BuscarPorCadena(cadena,fichero):
	lista=[]
	lista2 = fichero.xpath("/menu/game")
	for a in lista2:
		if a.xpath("./@name")[0].startswith(cadena):
			dicc={}
			dicc['nombre']=a.xpath("./description/text()")
			dicc['año']=a.xpath("./year/text()")
			dicc['desarrolladora']=a.xpath("./dev/text()")
			lista.append(dicc)
	return lista

def BuscarPorGenero(genero,fichero):
	lista=[]
	lista2 = fichero.xpath("/menu/game")
	for a in lista2:
		if genero in a.xpath("./genre/text()"):
			lista.append(a.xpath("./description/text()"))
	return lista					
