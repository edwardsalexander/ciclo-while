#Escribe un programa que solicite al usuario un número entero positivo 
# y luego imprima la suma de los primeros
# n números pares utilizando un bucle while.

numero = int(input("Por favor, ingresa un número entero positivo: "))


if numero > 0:
    suma = 0  
    contador = 0  
    num_actual = 2  

    while contador < numero:
        suma += num_actual 
        num_actual += 2
        contador += 1 

    print(f"La suma de los primeros {numero} números pares es: {suma}")
else:
    print("error en el  numero")
