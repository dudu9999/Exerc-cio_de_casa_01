#13	Ler um número N e imprimir F1, F2 ou F3, conforme a condição:
#	se N <= 10 imprima F1,
#	se N > 10 e <= 100 imprima F2
#	se N >100 imprima F3.

N = 0

N = int(input("Digite um numero: "))

if N <= 10:
	print("        __ ")
	print("      | F1 |")
	print("        -- ")
elif N > 10 and N < 100:
	print("        __ ")
	print("      | F2 |")
	print("        -- ")
else:
	print("        __ ")
	print("      | F3 |")
	print("        -- ")

