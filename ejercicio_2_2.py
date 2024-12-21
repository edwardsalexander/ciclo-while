#Escribe un programa que solicite al usuario dos números enteros positivos
# y luego imprima todos los números entre ellos (inclusive) utilizando un bucle while.


numero1 = int(input("primer numero: "))
numero2 = int(input("segundo numero: "))

if numero1 > 0 and numero2 > 0:
    inicio = min(numero1, numero2)
    fin = max(numero1, numero2)

    while inicio <= fin:
        print(inicio)
        inicio += 1
else:
    print("error")
