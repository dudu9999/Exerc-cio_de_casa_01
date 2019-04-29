#12.	1.1 - Maria quer saber quantos litros de gasolina precisa colocar em seu 
#carro e quanto vai gastar para fazer uma viagem até a casa de sua irmã.

#Dados extras:
#Distância da casa de Maria até sua irmã : 520 km
#Seu carro consome 12 Km/litro de combustível.
#Ela abastece sempre no mesmo posto, onde o preço da gasolina é R$ 2,50 o litro.

#1.2 - Desenvolva um algoritmo onde o usuário digite a distância, o consumo e o
#valor do litro de combustível, com estes dados o algoritmo deverá calcular 
#a quantidade de litros de combustível para a viagem e o custo da viagem.

print("Exercicio 1.1 \n")
print("Maria quer saber quantos litros de gasolina precisa colocar em seu carro e quanto vai gastar para fazer uma viagem até a casa de sua irmã.")

litro_necessario = 0

print("Com base que a distância da casa de Maria até sua irmã é 520 km e o preço da gasolina é 2,50 eo carro dela faz 12 km/litro ")

distancia = 520
faz_por_litro = 12
preco_gas = 2.50
#preco_gas = 2
litro_distancia = 0

litro_distancia = (distancia / faz_por_litro)

litro_necessario = (litro_distancia * preco_gas)

print("Maria vai precisar colocar ",int(litro_distancia)," litros de gasolina e ela vai gastar ",int(litro_necessario)," Reais para essq viagem.")

print("para chegar na casa de sua irmã.")
#--------------------------------------------------------
print("\nExercicio 1.2 \n")

distancia, valor_do_litro, distancia_local_necessario, combustivel_necessario = 0, 0, 0, 0 

distancia_local = int(input("digite a distância do local que voce vai dirigir: "))
qnto_carro_faz_por_litro = int(input("digite o consumo(quanto seu carro faz por litro): "))
valor_do_litro = float(input("digite o valor do litro da gasolina: "))

distancia_local_necessario = (distancia_local / qnto_carro_faz_por_litro)

Valor_necessario_viagem = (litro_distancia * valor_do_litro)

print("Você vai precisar colocar ",int(distancia_local_necessario)," litros de gasolina e você vai gastar ",int(Valor_necessario_viagem)," Reais para essq viagem.")

print("para chegar na casa de sua irmã.")
#a quantidade de litros de combustível para a viagem e o custo da viagem.
