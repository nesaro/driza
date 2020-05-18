#!/usr/bin/python
# -*- coding: utf-8 -*-

#Copyright (C) 2006-2007   Néstor Arocha Rodríguez, Inmaculada Luengo Merino
#This file is part of Driza.
#
#Driza is free software; you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation; either version 2 of the License, or
#(at your option) any later version.
#
#Driza is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with Driza; if not, write to the Free Software
#Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

"""Estudio descriptivo de variables"""
nombre="Descriptivo"
tipo="Calculo"
etiquetas=["Descriptivos"]

#Definicion widget
doc={
        "nombre":u"Centralización",
        "tipo":"SeleccionMultiple",
        "opciones":["Media","Mediana","Moda"]}
dod={
        "nombre":u"Dispersión",
        "tipo":"SeleccionMultiple",
        "opciones":["Varianza",u"Desviación",u"Máximo",u"Mínimo","Rango"]}
percentil={"nombre":"Percentil","tipo":"EntradaTexto"}
dof={
        "nombre":"Forma",
        "tipo":"SeleccionMultiple",
        "opciones":["Curtosis",u"Coeficiente de Asimetría"]}
widget={"tipo":"Variable","opciones":[doc,dod,dof,percentil]}

#Definicion del formato de resultados
definicionresultado = [
        {"tipo":"Tabla","nombre":"Descriptivo","autoencoger":True,
         "disposicion":"Vertical",
         "cabecera":["Variable",u"Número de casos","Media","Varianza",u"Desviación","Mediana","Moda",
                     "Rango",u"Máximo",u"Mínimo","Percentil","Curtosis",u"Coeficiente de Asimetría"]}]


def funcionprincipal(dato, variable, opciones):
    from rpy import r  #pylint: disable=import-error
    import statistics
    diccionario={"Descriptivo":{"Media":None,"Varianza":None,u"Desviación":None,"Mediana":None,
                                "Moda":None,"Rango":None,u"Máximo":None,u"Mínimo":None,"Percentil":None,
                                "Curtosis":None,u"Coeficiente de Asimetría":None}}
    lista=dato.query(variable)
    diccionario["Descriptivo"]["Variable"]=str(variable)
    diccionario["Descriptivo"][u"Número de casos"]=len(lista)
    if "Media" in opciones: diccionario["Descriptivo"]["Media"]=r.mean(lista)
    if "Varianza" in opciones: diccionario["Descriptivo"]["Varianza"]=r.var(lista)
    if u"Desviación" in opciones: diccionario["Descriptivo"][u"Desviación"]=r.sd(lista)
    if "Mediana" in opciones: diccionario["Descriptivo"]["Mediana"]=r.median(lista)
    #http://cran.r-project.org/doc/contrib/Lemon-kickstart/kr_dstat.html
    #http://wiki.r-project.org/rwiki/doku.php?id=tips:stats-basic:modalvalue&s=modal
    if "Moda" in opciones:
        diccionario["Descriptivo"]["Moda"]=statistics.mode(lista)
    if "Rango" in opciones: diccionario["Descriptivo"]["Rango"]=r.range(lista)
    if u"Máximo" in opciones: diccionario["Descriptivo"][u"Máximo"]=r.max(lista)
    if u"Mínimo" in opciones: diccionario["Descriptivo"][u"Mínimo"]=r.min(lista)
    if "Percentil" in opciones: diccionario["Descriptivo"]["Percentil"]="TODO"
    if "Curtosis" in opciones:
        r.require("e1071")
        diccionario["Descriptivo"]["Curtosis"]=r.kurtosis(lista)
    if u"Coeficiente de Asimetría" in opciones:
        r.require("e1071")
        diccionario["Descriptivo"][u"Coeficiente de Asimetría"]=r.skewness(lista)

    return diccionario


def funcionchequeoentradausuario(opciones):  
    return True

def funcionchequeocondiciones(interfazdato):
    return True

