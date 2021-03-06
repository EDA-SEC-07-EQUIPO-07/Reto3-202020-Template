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

import config as cf
from App import model
import datetime
import csv

"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta.  Esta responsabilidad
recae sobre el controlador.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________


def init():
    """
    Llama la funcion de inicializacion del modelo.
    """
    analyzer = model.newAnalyzer()
    return analyzer


# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________

def loadData(analyzer, accident_file):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    accident_file = cf.data_dir + accident_file
    input_file = csv.DictReader(open(accident_file, encoding="utf-8"),
                                delimiter=",")
    for accident in input_file:
        model.addAccident(analyzer, accident)
    return analyzer


# ___________________________________________________
#  Funciones para consultas
# ___________________________________________________

def getAccidentsSize(analyzer):
    retorno = model.accidentsSize(analyzer)
    return retorno

def getIndexSize(analyzer):
    retorno = model.indexSize(analyzer)
    return retorno
  
def getindexheight(analyzer):
    retorno = model.indexheight(analyzer)
    return retorno

def getHourSize(analyzer):
    retorno = model.hourSize(analyzer)
    return retorno
    
def getAccidentsByDate(analyzer, fecha):
    retorno = model.AccidentsByDate(analyzer, fecha)
    return retorno

def getAccidentsBeforeADate(analyzer, fecha):
    retorno = model.AccidentsBeforeADate(analyzer, fecha)
    return retorno

def getAccidentsInRange(analyzer, fecha_inicio, fecha_fin):
    retorno = model.AccidentsInRange(analyzer, fecha_inicio, fecha_fin)
    return retorno

def getAccidentsbystate(analyzer, fecha_inicio, fecha_fin):
    retorno = model.accidentstate(analyzer, fecha_inicio, fecha_fin)
    return retorno

def getAccidentsByHour(analyzer, hora_inicio, hora_fin):
    retorno = model.Accidentesporcategoria(analyzer, hora_inicio, hora_fin)
    return retorno
