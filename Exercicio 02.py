'''2.	Escreva um algoritmo que leia dois nÃºmeros que 
deverÃ£o ser colocados, respectivamente, nas variÃ¡veis VA 
e VB.O algoritmo deve, entÃ£o, trocar os valores de VA por VB 
e vice-versa e mostrar o conteÃºdo destas variÃ¡veis.'''

VA, VB, VC = 0, 0, 0
VA = int(input("digite um bumero: "))
VB = int(input("digite outro bumero: "))
VC = VA
VA = VB
VB = VC

print("Primeiro numero",VA,"segundo numero",VB)
