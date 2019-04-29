# 6 - Fazer um algoritmo para ler dois números e mostrar o maior deles.
n1, n2, = 0, 0


n1 = int(input("1 - Digite um numero: "))
n2 = int(input("2 - Digite um numero: "))

if n1<n2:
    print("O Primeiro numeros e maior que o segundo ",n1,">",n2)
else:
    print("O Primeiro numeros e menor que o segundo ",n1,"<",n2)

