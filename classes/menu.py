# -*- coding: utf-8 -*-

class Menu:
  def __init__(self, laboratorio):
    self.laboratorio = laboratorio

  def ver(self):
    print(' Bienvenido al sistema '.center(50,'='))
    print('Laboratorio: ' + self.laboratorio)
    print('¿Cual tipo de usuario eres?')
    print('1. Técnico')
    print('2. Estudiante')
    op = input(">>>> ")
    return op

class MenuTecnicos:
  def ver(self):
    print(' Menú técnicos de laboratorio '.center(50,'='))
    print('¿Qué deseas hacer?')
    print('1. Comprar equipo')
    print('2. Registrar prestamo')
    print('3. Registrar mantenimiento')
    print('4. Ver equipos')
    print('5. Ver prestamos')
    print('6. Ver mantenimientos en un rango de fechas')
    op = input(">>>> ")
    return op

class MenuEstudiantes:
  def ver(self):
    print(' Menú estudintes '.center(50,'='))
    print('¿Qué deseas hacer?')
    print('1. Consultar tus prestamos de equipos')
    print('2. Ver equipos disponilbes')
    op = input(">>>> ")
    return op

if __name__ == '__main__':
  m = Menu('xxxx')
  m.ver() 