#Escribe un programa que solicite al usuario un número entero positivo y luego 
#imprima los primeros n números impares utilizando un bucle while

numero = int(input("Por favor, ingresa un número entero positivo: "))


if numero > 0:
    contador = 0
    num_actual = 1  

    while contador < numero:
        print(num_actual) 
        num_actual += 2 
        contador += 1  
else:
    print("fallo.")


