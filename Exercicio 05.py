# 5 - Ler um conjunto de 5 dados numéricos e imprimir sua soma e sua média.
n1, n2, n3, n4, n5, res = 0, 0, 0, 0, 0, 0


n1 = int(input("1 - Digite um numero: "))
n2 = int(input("2 - Digite um numero: "))
n3 = int(input("3 - Digite um numero: "))
n4 = int(input("4 - Digite um numero: "))
n5 = int(input("5 - Digite um numero: "))

res = ((n1+n2+n3+n4+n5)/5)

print("A media aritmetica dos cinco numeros e: ",res)