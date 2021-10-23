#Crie um programa que armazene em uma tupla os meses do ano e informe o mês por
#extenso. Por exemplo, se o usuário digitar 6 o programa deve exibir junho. Se ele digitar um
#valor menor que 1 e maior que 13, o programa deve exibir uma mensagem de erro.

meses = ('janeiro', 'fevereiro', 'março',
        'abril', 'maio', 'junho', 'julho',
        'agosto', 'setembro', 'outubro',
        'novembro', 'janeiro')
while True:
    numero = int(input("Digite um número entre 1 e 12: ")) - 1
    
    if 0 <= numero <= 12:
        break
    print("Tente novamente.", end='')
    
print(f'Você digitou o mês {meses[numero]}')
