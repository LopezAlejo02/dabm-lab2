# -*- coding: utf-8 -*-
from tabulate import tabulate

class Estudiante:
    file = 'Database\Prestamos.csv'
    def __init__(self, nombre, numeroDeCarnet):
        self.nombre = nombre
        self.numeroDeCarnet = numeroDeCarnet

    def consultarPrestamo(self):
        f = open(self.file,'r')
        prestamos = f.readlines()
        matriz = []
        for l in prestamos:
            lista = l.split(';')
            if lista[1] == self.numeroDeCarnet:
                matriz.append(lista)
        headers = ['Estudiante', 'carnet', 'Fecha de prestamo', 'Equipo', 'Referencia del equipo']
        print(tabulate(matriz, headers, tablefmt="grid"))

def crearEstudiante():
    print('Ingresa tu nombre por favor: ')
    nombre = input('>>>> ')
    print('¡Hola ' + nombre + '! Ingresa tu número de carnet por favor: ')
    carnet = input('>>>> ')
    est = Estudiante(nombre, carnet)
    return est

def verEquiposDisp():
    datosEquipos = open('Database\Equipos.csv', 'r')
    equipos = datosEquipos.readlines()
    matriz = []
    for l in equipos:
        lista = l.split(';')
        if lista[4] != '0':
            matriz.append(lista)
    headers = ['Nombre', 'Refenerncia', 'Proveedor', 'Ciclo', 'Cantidad', 'Fecha ult. mant.']
    print(tabulate(matriz, headers, tablefmt="grid"))