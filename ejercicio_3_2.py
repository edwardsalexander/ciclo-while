#Escribe un programa que solicite al usuario un número entero positivo 
#y luego calcule la suma de todos los 
#números divisibles por 3 desde 1 hasta ese número utilizando un bucle while.

# Solicitar al usuario un número entero positivo
numero = int(input("Por favor, ingresa un número entero positivo: "))

# Verificar que el número sea positivo
if numero > 0:
    suma = 0
    i = 1
    while i <= numero:
        if i % 3 == 0: 
            suma += i   
        i += 1  


    print("La suma de los números divisibles por 3 entre 1 y", numero, "es:", suma)
else:
    print("error")
