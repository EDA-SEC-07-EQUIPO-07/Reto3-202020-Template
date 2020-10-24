"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import sys
import config
from DISClib.ADT import list as lt
from App import controller
assert config

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones  y  por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________


accident_file = 'us_accidents_small.csv'

# ___________________________________________________
#  Menu principal
# ___________________________________________________


def printMenu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar información de accidentes")
    print("3- Accidentes ocurridos en una fecha especifica")
    print("4- Accidentes ocurridos antes de una fecha")
    print("5- Prueba")
    print("0- Salir")
    print("*******************************************")
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n>')

    if int(inputs[0]) == 1:
        print("\nInicializando....")
        # cont es el controlador que se usará de acá en adelante
        cont = controller.init()

    elif int(inputs[0]) == 2:
        print("\nCargando información de accidentes ....")
        controller.loadData(cont, accident_file)
        print('Accidentes cargados: ' + str(controller.getAccidentsSize(cont)))
        
    elif int(inputs[0]) == 3:
        print("\nBuscando accidentes en un rango de fechas: ")
        Fecha = input('Ingrese la fecha sobre la cual desea saber cuantos accidentes hubo: ')
        print(controller.getAccidentsByDate(cont, Fecha))

    elif int(inputs[0]) == 4:
        print("\nBuscando accidentes anteriores a una fecha: ")
        Fecha = input('Ingrese una fecha para saber la cantidad de accidentes y el día con más accidentes anteriores a esa fecha: ')
        print(controller.getAccidentsBeforeADate(cont, Fecha))
        
    elif int(inputs[0]) == 5:
        print(controller.prueba(cont))
    else:
        sys.exit(0)
        
sys.exit(0)







def AccidentsInRange(analyzer, fecha_ini, fecha_fin):
    dictfechatot={'Total accidentes entre la fecha ingresa:':None,
                  'Categoría más reportada:':None}
    fechauno=datetime.datetime.strptime(fecha_ini,'%Y-%m-%d')
    fechados=datetime.datetime.strptime(fecha_fin,'%Y-%m-%d')
    fecha_menor=str(om.minKey(analyzer['dateIndex']))
    fecha_min=datetime.datetime.strptime(fecha_menor,'%Y-%m-%d')
    if fecha_min>fechados:
        return "No hay fechas anteriores a la ingresada"
    dategetter=om.values(analyzer['dateIndex'],fechauno.date(),fechados.date())
    num_fechas=lt.size(dategetter)
    i=1
    num_mayor=0
    total=0
    category=0
    categorias=[]
    while i<=num_fechas:
        elements=lt.getElement(dategetter,i)
        lista=elements['lstaccidents']
        num_accident=lt.size(lista)
        total+=num_accident
        categories=lt.getElement(lista,i)
        categorias.append(categories['Severity'])   
        if num_accident>num_mayor:
                num_mayor=num_accident    
        i += 1
    category=max(categorias)
    dictfechatot['Total accidentes entre la fecha ingresada:']=total
    dictfechatot['Categoría más reportada:']=category
    return dictfechatot

def Accidentesporcategoria (analyzer, Tinit, Tfin):
    dicc = {'1': None, '2': None, '3': None, '4': None}
    t_min=datetime.datetime.strptime(Tinit,'%H:%M')
    t_max=datetime.datetime.strptime(Tfin,'%H:%M')
    dategetter=om.values(analyzer['hourIndex'],t_min.date(),t_max.date())
    cantidad=lt.size(dategetter)
    i=1
    while i <=cantidad:
        
    return dicc
