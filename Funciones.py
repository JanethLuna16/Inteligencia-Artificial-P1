
from tkinter import Y
from turtle import ycor


def suma(x,y):                                      #Funcion Con parametros y con retorno se muestra solo el retorno de la funci�n pero fuera de la funci�n tu le asignas losparametros que desees
    return x+y
total = suma (15,20)                                #Se asignan los parametros a la funci�n
print ("Suma:\n",total)

def resta(x,y):                                     #Funcion Con parametros y sin retorno Se muestra a TODA la funcion, pero tu le asignas los parametros de cada variable
    print("Resta:\n",x-y)
resta(15,20)                                        #Se asignan los parametros a la funci�n

def multi():                                        #Funcion sin parametros y sin retorno, cuando se llama a la funci�n, se muestran TODA las instrucciones que esten dentro de ella
    a=15
    b=20
    print("Multiplicacion:\n" , a*b)
multi()                                             #Mandamos a llamar a la funci�n en cualquier parte del programa

def div():                                           #Funcion sin parametros y con retorno, declaramos las variables y retorna SOLO el resultado cuando llamas la funcion
    a=15
    b=20
    return a/b

print("Division:\n", div())                         #Madamos a llamar a la funci�n en cualquier parte del programa