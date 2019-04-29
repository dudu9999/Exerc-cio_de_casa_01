#Escrever um algoritmo para ler uma #temperatura em 
#Fahrenheit e apresentá-la convertida em graus Centígrados.
#Fórmula:
#Centígrados =	((Fahrenheit – 32) x 5)/9

tempF, tempG = 0, 0

tempF = int(input("Digite a temperatura em Fahrenheit: "))
tempG = (((tempF - 32)*5)/9)

print(tempF,"Fahrenheit Convertido em Graus centigrados e igual a ",tempG)


