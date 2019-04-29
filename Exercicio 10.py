#10. Fazer um algoritmo para ler duas notas, os pesos de
# cada nota e mostrar a média ponderada.
#                              (nota 1 * peso da nota 1) + (nota 2 * peso da nota 2)
#Cálculo da Média Ponderada = -------------------------------------------------------
#                                        soma dos pesos

nota1, nota2, peso1, peso2, pesos,res = 0, 0, 0, 0, 0, 0

nota1 = int(input("1.1 - digite a nota da primira prova: "))
peso1 = int(input("1.2 - digite o peso da primira prova: "))
nota2 = int(input("2.1 - digite a nota da segunda prova: "))
peso2 = int(input("2.2 - digite o peso da primira prova: "))
pesos = (peso1+peso2)
res = (((nota1 * peso1)+(nota2 * peso2))/pesos)

print("Sua nota final e: ",res)
