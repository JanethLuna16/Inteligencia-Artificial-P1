#!/usr/bin/env phyton
# _*_ coding: cp1252 _*_           #Librerias para los acentos
# _*_ coding: 850 _*_
# _*_ coding: utf-8 _*_ 

nombre = input("\t Ingresa su Nombre \n ")              #Input se utiliza para que el usuario ingrese valores, como es de tipo string no es necesario
Nombre =["No�","Jes�s","Alan","Janeth", "Fernando"]     #Declaraci�n de lista 

if  nombre in Nombre:
    print("El nombre que ingresaste esta en la Lista")  #Comparaci�n de dato ingresado con la lista , si el nombre esta en la lista, se ejecuta la instrucci�n

else: 
    print("Nombre no registrado ")                      #Si el nombre no esta en la lista, se salta al esle para ejecutar la siguiente instrucci�n
