#Escribe un programa que solicite 
#al usuario un número entero positivo y luego imprima todos los números entre 1 
#y ese número que sean múltiplos de 5 utilizando un bucle while.

numero = int(input("Por favor ingresa un número : "))

if numero > 0:
    i = 1
    while i <= numero:
        if i % 5 == 0:
            print(i)
        i += 1
else:
    print("no hay numero multiple de 5.")
