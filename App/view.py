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


accident_file = 'us_accidents_dis_2016.csv'

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
    print("5- Accidentes en un rango de fechas")
    print("6- Estado con más accidentes")
    print("7- Accidentes en un rango de horas")
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
        print('Elementos en el arbol de fechas: ' + str(controller.getIndexSize(cont))) 
        print('Elementos en el arbol de horas: ' + str(controller.getHourSize(cont)))
        
    elif int(inputs[0]) == 3:
        print("\nBuscando accidentes en un rango de fechas: ")
        Fecha = input('Ingrese la fecha sobre la cual desea saber cuantos accidentes hubo: ')
        print(controller.getAccidentsByDate(cont, Fecha))

    elif int(inputs[0]) == 4:
        print("\nBuscando accidentes anteriores a una fecha: ")
        Fecha = input('Ingrese una fecha para saber la cantidad de accidentes y el día con más accidentes anteriores a esa fecha: ')
        print(controller.getAccidentsBeforeADate(cont, Fecha))
    elif int(inputs[0]) == 5:
        print("\nBuscando accidentes en un rango de fechas: ")
        fecha1 = input('Ingrese una fecha desde la que desea empezar a buscar: ')
        fecha2 = input('Ingrese una fecha en la que desea dejar de buscar: ')
        print(controller.getAccidentsInRange(cont, fecha1, fecha2))
    elif int(inputs[0]) == 6:
        print("\nBuscando estado con más accidentes: ")
        fecha1 = input('Ingrese una fecha desde la que desea empezar a buscar: ')
        fecha2 = input('Ingrese una fecha en la que desea dejar de buscar: ')
        print(controller.getAccidentsbystate(cont, fecha1, fecha2))
    elif int(inputs[0]) == 7:
        print("\nBuscando accidentes en un rango de horas: ")
        hora1 = input('Ingrese una hora desde la que desea empezar a buscar: ')
        hora2 = input('Ingrese una hora en la que desea dejar de buscar: ')
        print(controller.getAccidentsByHour(cont, hora1, hora2))

    else:
        sys.exit(0)
        
sys.exit(0)
