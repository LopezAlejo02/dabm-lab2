# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 09:36:47 2022

@author: Alejandro López
"""

from classes.equipo import crearEquipo, verEquipos, mantenimiento, rangoMant
from classes.menu import Menu, MenuTecnicos, MenuEstudiantes
from classes.prestamo import verPrestamos, crearPrestamo
from classes.estudiante import crearEstudiante, verEquiposDisp

if __name__ == '__main__':
  menu = Menu('Escuela de ingeniería')
  op = menu.ver()
  if op == '1':
    menu2 = MenuTecnicos()
    op2 = menu2.ver()
    if op2 == '1':
        e = crearEquipo()
        e.save()
    elif op2 == '2':
        p = crearPrestamo()
        p.save()
    elif op2 == '3':
        mantenimiento()
    elif op2 == '4':
        verEquipos()
    elif op2 == '5':
        verPrestamos()
    elif op2 == '6':
        rangoMant()
    else:
        print('Opción incorrecta')
  elif op == '2':
      est = crearEstudiante()
      menu3 = MenuEstudiantes()
      op3 = menu3.ver()
      if op3 == '1':
          est.consultarPrestamo()
      elif op3 == '2':
          verEquiposDisp()
      else:
          print('Opción incorrecta')
  else:
    print('Opción incorrecta')