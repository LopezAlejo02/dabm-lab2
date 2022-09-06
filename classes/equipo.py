from datetime import datetime, timedelta
from tabulate import tabulate
class Equipo:
    file = 'Database/Equipos.csv'
    def __init__(self, nombre, referencia, proveedor, cicloMan):
        self.nombre = nombre
        self.referencia = referencia
        self.proveedor = proveedor
        self.cicloMan = cicloMan
        self.fum = datetime.now().strftime('%d/%m/%Y')

    def save(self):
        f = open(self.file,'a')
        agregar = [self.nombre,self.referencia, self.proveedor, self.cicloMan, datetime.datetime.now().strftime('%d/%m/%Y')]
        equipo = ';'.join(agregar)
        f.write(equipo + '\n')
        f.close()
def crearEquipo():
    nombre = input('Ingrese el nombre del equipo: ')
    referencia = input('Ingrese la referencia del equipo: ')
    proveedor = input('Ingrese el proveedor del equipo: ')
    cicloMan = input('Ingrese el ciclo de mantenimiento del equipo: ')
    e = Equipo(nombre, referencia, proveedor, cicloMan)
    return e

def verEquipos():
    f = open('Database/Equipos.csv','r')
    equipos = f.readlines()
    f.close()
    headers = ['Nombre', 'Referencia','Proveedor','Ciclo de Mantenimiento','Fecha de último mantenimiento']
    matriz = []
    for i in equipos:
        l = i.split(';')
        matriz.append(l)
    print(tabulate(matriz, headers, tablefmt="grid"))

def mantenimiento():
    f = open('Database/Equipos.csv','r')
    equipos = f.readlines()
    f.close()

    matriz = []
    for i in equipos:
        l = i.split(';')
        matriz.append(l)
    mant = input('Ingrese el nombre del equipo: ')
    ref = input('Ingrese la referencia del equipo: ')
    cambio = []
    for i in range(0,len(matriz)):
        if mant == matriz[i][0] and ref == matriz[i][1]:
            cambio = matriz[i]
    cambio[4] = input('Ingrese la fecha de mantenimiento (dd/mm/aaaa): ')
    cambio.append('\n')
    matriz.insert(i,cambio)
    matriz.pop(i+1)

    f = open('Database/Equipos.csv', 'w')
    for j in range(0,len(matriz)):
        f.write(';'.join(matriz[j]))

    f.close()

def rangoMant():
    f = open('Database/Equipos.csv','r')
    equipos = f.readlines()
    f.close()
    matriz = []
    for i in equipos:
        l = i.split(';')
        matriz.append(l)
    print('Ingrese el rango en el cual desea buscar')
    fecha_ini = datetime.strptime(input('Ingrese la fecha de inicio (dd/mm/aaaa): '), '%d/%m/%Y')
    fecha_fin = datetime.strptime(input('Ingrese la fecha final (dd/mm/aaaa): '), '%d/%m/%Y')
    mant = []
    for i in range(0,len(matriz)):
        if fecha_ini >= timedelta(days = int(matriz[i][3])) + datetime.strptime(matriz[i][4], '%d/%m/%Y'):
            if fecha_fin <= timedelta(days = int(matriz[i][3])) + datetime.strptime(matriz[i][4], '%d/%m/%Y'):
                mant.append(matriz[i])

    headers = ['Nombre', 'Referencia', 'Proveedor', 'Ciclo de Mantenimiento', 'Fecha de último mantenimiento']
    print(tabulate(matriz, headers, tablefmt="grid"))