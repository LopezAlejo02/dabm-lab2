# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 14:11:16 2022

@author: Alejandro López
"""
from tabulate import tabulate

class Prestamo:
    file = 'Database\Prestamos.csv'
    def __init__(self, estudiante, carnet, fechaPrestamo, equipo, refEquipo):
        self.estudiante = estudiante
        self.carnet = carnet
        self.fechaPrestamo = fechaPrestamo
        self.equipo = equipo
        self.refEquipo = refEquipo
    def save(self):
        f = open(self.file,'a')
        linea = ';'.join([self.estudiante,self.carnet,self.fechaPrestamo,self.equipo,self.refEquipo])
        f.write(linea+'\n')
        f.close()
def verPrestamos():
    f = open('Database\Prestamos.csv', 'r')
    prestamos = f.readlines()
    matriz = []
    for l in prestamos:
        lista = l.split(';')
        matriz.append(lista)
    headers = ['Estudiante', 'carnet', 'Fecha de prestamo', 'Equipo', 'Referencia del equipo']
    print(tabulate(matriz, headers, tablefmt="grid"))

def crearPrestamo():
    print('Registrar prestamo')
    nombre = input('Estudiante: ')
    carnet = input('Carnet: ')
    fechaPrestamo = input('Fecha de prestamo: ')
    equipo = input('Equipo: ')
    referencia = input('Referencia del equipo: ')
    p = Prestamo(nombre, carnet, fechaPrestamo, equipo, referencia)
    return p