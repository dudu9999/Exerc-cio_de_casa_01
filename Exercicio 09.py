#Faça um algoritmo que mostre o resultado da expressão abaixo:
# (( x – 5) * y) – z
# Obs: Ler valores para as variáveis x, y e z.

X, Y, Z, res = 0, 0, 0, 0

X = int(input("digite um numero: "))
Y = int(input("digite outro numero: "))
Z = int(input("digite so mais um numero: "))
res = (((X-5)*Y)-Z)

print("O resultado e: ",res)
