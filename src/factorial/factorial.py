#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys
def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return 0
    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

if len(sys.argv) == 1: #0 nunca va a ser xq tiene al menos el nombre del programa
   print("Debe ingresar un número o rango de números para calcular")
   sys.exit()

input = sys.argv[1] #toma lo ingresado

# el usuario pasa un rango
if "-" in input: #si está dividido, es decir si hay rango
    desde, hasta = input.split("-") 
    
    desde = int(desde) #toma ccada número como entero
    hasta = int(hasta)

    if desde > hasta:
        print("El rango ingresado no es correcto")
        sys.exit()

    for n in range(desde, hasta + 1):
        print("factorial", n, "! =", factorial(n))

else:   # si solo hay un número 
    num = int(input)
    print("factorial", num, "! =", factorial(num))