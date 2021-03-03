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