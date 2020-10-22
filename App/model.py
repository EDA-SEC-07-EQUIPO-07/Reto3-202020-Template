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
import config
from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import map as m
import datetime
assert config

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria


"""

# -----------------------------------------------------
# API del TAD Catalogo de accidentes
# -----------------------------------------------------

def newAnalyzer():
    analyzer = {'Accidents': None,
                'dateIndex': None}
    analyzer['Accidents'] = lt.newList('SINGLE_LINKED', compareIds)
    analyzer['dateIndex'] = om.newMap(omaptype='BST',
                                      comparefunction=compareDates)
    return analyzer

# Funciones para agregar informacion al catalogo

def addAccident(analyzer, accident):
    lt.addLast(analyzer['Accidents'], accident)
    updateDateIndex(analyzer['dateIndex'], accident)
    return analyzer


def updateDateIndex(map, accident):
    occurreddate = accident['Start_Time']
    accidentdate = datetime.datetime.strptime(occurreddate, '%Y-%m-%d %H:%M:%S')
    entry = om.get(map, accidentdate.date())
    if entry is None:
        datentry = newDataEntry(accident)
        om.put(map, accidentdate.date(), datentry)
    else:
        datentry = me.getValue(entry)
    addDateIndex(datentry, accident)
    return map


def addDateIndex(datentry, accident):
    lst = datentry['lstaccidents']
    lt.addLast(lst, accident)
    return datentry


def newDataEntry(accident):
    """
    Crea una entrada en el indice por fechas, es decir en el arbol
    binario.
    """
    entry = {'lstaccidents': None}
    entry['lstaccidents'] = lt.newList('SINGLE_LINKED', compareDates)
    return entry

# ==============================
# Funciones de consulta
# ==============================

def accidentsSize(analyzer):
    return lt.size(analyzer['Accidents'])

def indexSize(analyzer):
    return om.size(analyzer['dateIndex'])

def indexheight(analyzer):
    return om.height(analyzer['dateIndex'])

def AccidentsByDate (analyzer,fecha):
    tupla=()
    fecha_acc=datetime.datetime.strptime(fecha,'%Y-%m-%d')
    fecha1=om.get(analyzer['dateIndex'],fecha_acc.date())
    lista_fecha=fecha1['value']
    a=lista_fecha['lstaccidents']
    b=lt.size(a)
    severidad=[]
    i=1
    while i<=b:
        getter=lt.getElement(a,i)
        severidad_num=getter['Severity']
        severidad.append(severidad_num)
        i+=1
    tupla=("Cantidad:"+str(b),"Severidad en cada caso:",severidad)
    return tupla
   
 def porcentaje (analyzer, dicc):
    lista = om.valueSet(analyzer ['dateIndex'])
    total = lt.size(lista)
    listados = dicc.values()
    tamaño = len(listados) 
    v = 0
    while v< tamaño:
        suma += listados[v]
    percent = 100*suma/total  
    tupla = (dicc, percent)
    return tupla  

# ==============================
# Funciones de Comparacion
# ==============================
def compareIds(id1, id2):
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1


def compareDates(date1, date2):
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1
