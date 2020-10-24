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
                'dateIndex': None,
                'hourIndex':None}
    analyzer['Accidents'] = lt.newList('SINGLE_LINKED', compareIds)
    analyzer['dateIndex'] = om.newMap(omaptype='BST',
                                      comparefunction=compareDates)
    analyzer['hourIndex'] = om.newMap(omaptype='BST',
                                      comparefunction=compareHours)
    return analyzer

# Funciones para agregar informacion al catalogo

def addAccident(analyzer, accident):
    lt.addLast(analyzer['Accidents'], accident)
    updateDateIndex(analyzer['dateIndex'], accident)
    updateHourIndex(analyzer['hourIndex'], accident)
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


def updateHourIndex(map, accident):
    occurreddate = accident['Start_Time']
    accidentdate = datetime.datetime.strptime(occurreddate, '%Y-%m-%d %H:%M:%S')
    time=str(accidentdate.hour)+':'+str(accidentdate.minute)
    accidenttime=datetime.datetime.strptime(time,'%H:%M')
    entry = om.get(map, accidenttime.time())
    if entry is None:
        datentry = newDataEntry(accident)
        om.put(map, accidenttime.time(), datentry)
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
    Crea una entrada en el indice por fechas o por hora, es decir en el arbol
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

def hourSize(analyzer):
    return om.size(analyzer['hourIndex'])

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

def AccidentsBeforeADate (analyzer,fecha):
    dictfechatot={'Total accidentes antes de la fecha ingresada:':None,
                  'Fecha con mas accidentes:':None}
    fecha_acc=datetime.datetime.strptime(fecha,'%Y-%m-%d')
    fecha_menor=str(om.minKey(analyzer['dateIndex']))
    fecha_maxima=str(om.maxKey(analyzer['dateIndex']))
    fecha_min=datetime.datetime.strptime(fecha_menor,'%Y-%m-%d')
    fecha_max=datetime.datetime.strptime(fecha_maxima,'%Y-%m-%d')
    if fecha_min==fecha_acc:
        return "No hay fechas anteriores a la ingresada"
    dategetter=om.values(analyzer['dateIndex'],fecha_min.date(),fecha_acc.date())
    num_fechas=lt.size(dategetter)
    i=1
    num_mayor=0
    total=0
    accidenteddate=None
    if fecha_acc>fecha_max:
        while i<=num_fechas:
            elements=lt.getElement(dategetter,i)
            lista=elements['lstaccidents']
            num_accident=lt.size(lista)
            total+=num_accident
            if num_accident>num_mayor:
                num_mayor=num_accident
                dates=lt.getElement(lista,1)
                x=datetime.datetime.strptime(dates['Start_Time'],'%Y-%m-%d %H:%M:%S')
                accidenteddate=x.date()
            i+=1
    else:
        while i<num_fechas:
            elements=lt.getElement(dategetter,i)
            lista=elements['lstaccidents']
            num_accident=lt.size(lista)
            total+=num_accident
            if num_accident>num_mayor:
                num_mayor=num_accident
                dates=lt.getElement(lista,1)
                x=datetime.datetime.strptime(dates['Start_Time'],'%Y-%m-%d %H:%M:%S')
                accidenteddate=x.date()
            i+=1
    dictfechatot['Total accidentes antes de la fecha ingresada:']=total
    dictfechatot['Fecha con mas accidentes:']=str(accidenteddate)
    return dictfechatot

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
        categorias.append(int(categories['Severity']))   
        if num_accident>num_mayor:
                num_mayor=num_accident    
        i += 1
    category=max(categorias)
    dictfechatot['Total accidentes entre la fecha ingresada:']=total
    dictfechatot['Categoría más reportada:']=category
    return dictfechatot

def Accidentesporcategoria (analyzer, Tinit, Tfin):
    dicc = {'1': 0, '2': 0, '3': 0, '4': 0}
    t_min=datetime.datetime.strptime(Tinit,'%H:%M')
    t_max=datetime.datetime.strptime(Tfin,'%H:%M')
    dategetter=om.values(analyzer['hourIndex'],t_min.time(),t_max.time())
    cantidad=lt.size(dategetter)
    i=1
    while i <=cantidad:
        elements=lt.getElement(dategetter,i)
        lista=elements['lstaccidents']
        categories=lt.getElement(lista,i)
        if categories['Severity'] == '1':
            dicc['1']+=1
        if categories['Severity'] == '2':
            dicc['2']+=1
        if categories['Severity'] == '3':
            dicc['3']+=1
        if categories['Severity'] == '4':
            dicc['4']+=1
    p = porcentaje(analyzer, dicc)
    return p

def accidentstate (analyzer, fechamin, fechamax):
    mapa = om.newMap(omaptype='BST', comparefunction=compareState)
    valor = om.values(analyzer ['dateIndex'], fechamin.date(), fechamax.date())
    i = 1
    fechas = lt.size(valor)
    while i<= fechas:
        elementos = lt.getElement(valor, i)
        accidentes = elementos['lstaccidents']
        tamaño = lt.size(accidentes)
        j = 1
        while j<= tamaño:
            caja = lt.getElement(accidentes, j)
            estado = caja['State']
            condicion = om.contains(mapa, estado)
            if condicion == False: 
                om.put(mapa, estado, 1)
            else:
                om.put(mapa, estado, +1)
            om.keySet
            j += 1
        i += 1

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


def compareHours(hour1, hour2):
    if (hour1 == hour2):
        return 0
    elif (hour1 > hour2):
        return 1
    else:
        return -1