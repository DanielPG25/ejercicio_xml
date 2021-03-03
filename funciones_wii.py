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

def BuscarPorJugadores(jugadores,fichero):
	lista=[]
	lista2 = fichero.xpath("/menu/game")
	for a in lista2:
		dicc={}
		dicc['nombre']=a.xpath("./description/text()")
		dicc['jug']=a.xpath("./player/text()")
		dicc['edad']=a.xpath("./rating/text()")
		lista.append(dicc)
	lista3=[]
	for b in lista:
		if jugadores == 1:
			dicc2={}
			dicc2['nombre']=b.get('nombre')[0]
			dicc2['jug']=b.get('jug')[0]
			dicc2['edad']=b.get('edad')[0]
			lista3.append(dicc2)
		elif b.get('jug')[0] != '1 Player':
			if jugadores <= int(b.get('jug')[0][2]) and jugadores < 10:
				dicc2={}
				dicc2['nombre']=b.get('nombre')[0]
				dicc2['jug']=b.get('jug')[0]
				dicc2['edad']=b.get('edad')[0]
				lista3.append(dicc2)
			if jugadores <= 10 and b.get('jug')[0] == '1-10 Players':
				dicc2={}
				dicc2['nombre']=b.get('nombre')[0]
				dicc2['jug']=b.get('jug')[0]
				dicc2['edad']=b.get('edad')[0]
				lista3.append(dicc2)
			if jugadores <= 12 and b.get('jug')[0] == '1-12 Players':
				dicc2={}
				dicc2['nombre']=b.get('nombre')[0]
				dicc2['jug']=b.get('jug')[0]
				dicc2['edad']=b.get('edad')[0]
				lista3.append(dicc2)					
	return lista3

def FiltrarPorEdad(edad,listadicc):
	lista=[]
	for a in listadicc:
		if edad == "Everyone":
			if a.get('edad')=="ESRB - E (Everyone)":
				lista.append(a.get('nombre'))
		elif edad in a.get('edad'):
			lista.append(a.get('nombre'))
	return lista						