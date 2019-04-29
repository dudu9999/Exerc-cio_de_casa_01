# 7 - Ler 3 números e imprimi-los em ordem crescente.
n1, n2, n3 = 0, 0, 0


n1 = int(input("1 - Digite um numero: "))
n2 = int(input("2 - Digite um numero: "))
n3 = int(input("3 - Digite um numero: "))
# 2  3  1
#n1 n2 n3
if (n1<n2) and (n2<n3) and (n1<n3):
    print("Em ordem crescente ",n1," ",n2," ",n3)
elif (n1<n2) and (n3<n2) and (n1<n3):
    print("Em ordem crescente ",n1," ",n3," ",n2)
elif (n2<n1) and (n2<n3) and (n1<n3):
    print("Em ordem crescente ",n2," ",n1," ",n3)
elif (n2<n1) and (n2<n3) and (n3<n1):
    print("Em ordem crescente ",n2," ",n3," ",n1)
elif (n3<n1) and (n3<n2) and (n1<n2):
    print("Em ordem crescente ",n3," ",n1," ",n2)    
else:
    print("Em ordem crescente ",n3," ",n2," ",n1)

