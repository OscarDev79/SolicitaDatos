# -*- coding: utf-8 -*-

# Hay que crear un programa que solicite los datos de un cliente:

#     Su nombre.
#     Su día, mes y año de nacimiento.

# Hay que almacenar los datos en variables.

# A continuación debemos mostrarle un mensaje personalizado indicando algo como:

# Saludos Juan, ya sé que tienes 20 años de edad

# Author Oscar Albarracin 

# Fecha: 21-10-2021


def solicita_informacion():
    nombre = input("Dime tu nombre: ")
    dia = int(input("Dime que dia naciste en numero: "))
    mes = int(input("Dime que mes nacieste en numero: "))
    anio = int(input("Dime que año naciste: "))
    return nombre, dia, mes, anio


def calculo_edad(dia, mes, anio):
    from datetime import date
    anio_actual = date.today().year
    mes_actual = date.today().month
    dia_actual = date.today().day
    edad = anio_actual - anio - ((mes_actual, dia_actual) < (mes, dia))
    return edad


def informe(nombre, edad):
    print("Saludos ", nombre, "ya se que tienes " + str(edad) + " años de edad")
    

nombre, dia, mes, anio = solicita_informacion()
edad = calculo_edad(dia, mes, anio)
informe(nombre, edad)
