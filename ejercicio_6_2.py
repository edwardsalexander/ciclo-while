#Escribe un programa que solicite al usuario un número 
# entero positivo y luego imprima la suma de los 
#cuadrados de todos los números desde 1 hasta ese número utilizando un bucle while
numero = int(input("Por favor, ingresa un número entero positivo: "))


if numero > 0:
    suma = 0
    i = 1

    while i <= numero:
        suma += i ** 2
        i += 1  
    print(f"La suma de los cuadrados de los números desde 1 hasta {numero} es: {suma}")
else:
    print("error.")
