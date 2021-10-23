#Faça um programa que preencha uma lista contendo um número indefinido de nome de
#carros e seus consumos (quantos km cada carro faz com 1 litro de combustível). Calcule e
#mostre: a. O modelo de carro mais econômico
#b. O modelo de carro menos econômico
#c. Quantos litros de combustível cada um dos carros cadastrados consome para
#percorrer uma distância de 1000 km

modelo_carro = []
consumo_km = []

print("Quando quiser sair do programa aperte enter.")

while True:
    modelo_carro.append(str(input('Digite o modelo do carro: ')))
    consumo_km.append(float(input('Digite o consumo do carro (km por litro): ')))
    resposta = str(input('Quer continuar? Sim ou Não\n'))
    if resposta in 'Não':
        print("Você encerrou o programa, aguarde.")
        break

resultado = ''
valor_gasolina = 7.00
total_km = 1000
for j, c in enumerate(modelo_carro):
    print('Veiculo {}'.format(j+1))
    print('Nome: {}'.format(c))
    print('Km por litro: {}\n'.format(consumo_km[j]))

    consumo = round(total_km/consumo_km[j], 2)
    resultado += 'O carro {} consome {}L e custará $R{} quando fizer {}km\n'.format(c, consumo, round(consumo*valor_gasolina, 2), total_km)

print('O carro mais econômico é o {}'.format(modelo_carro[consumo_km.index(max(consumo_km))]))
print('O carro menos econômico é o {}'.format(modelo_carro[consumo_km.index(min(consumo_km))]))
print(resultado)

