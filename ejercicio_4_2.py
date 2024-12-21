#Escribe un programa que solicite al usuario un número entero positivo y 
#luego imprima si el número es un número de Armstrong utilizando un bucle while.


numero = int(input("ingresar numero: "))

if numero > 0:
    numero_str = str(numero)
    
    num_digitos = len(numero_str)
    
    suma = 0
    temp = numero  

    while temp > 0:
        digito = temp % 10
        suma += digito ** num_digitos
        temp //= 10

    if suma == numero:
        print(f"{numero} es un número de Armstrong.")
    else:
        print(f"{numero} no es un número de Armstrong.")

