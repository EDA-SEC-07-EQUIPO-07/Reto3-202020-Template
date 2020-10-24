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


# Funciones para agregar informacion al catalogo


# ==============================
# Funciones de consulta
# ==============================
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

def compareState(name, State):
    stateEntry = me.getKey(state)
    if name == stateEntry:
        return 0
    elif name > stateEntry:
        return 1
    else:
        return -1
