#Escribe un programa que solicite 
#al usuario un número entero positivo y luego imprima todos los números 
#primos menores o iguales a ese número utilizando un bucle while.


numero = int(input("Por favor, ingresa un número entero positivo: "))


if numero > 0:
    num_actual = 2  

    while num_actual <= numero:
    
        es_primo = True
        divisor = 2
        
        while divisor <= num_actual // 2:
            if num_actual % divisor == 0:
                es_primo = False
                break
            divisor += 1
        
        if es_primo:
            print(num_actual)
        
        num_actual += 1  
else:
    print("error")
