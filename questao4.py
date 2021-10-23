#Crie uma tupla com os 15 primeiros países com mais medalhas no ranking das olimpíadas do
#Japão (2021). Informe nesta lista: i. os 3 primeiros colocados; ii. os 2 últimos colocados; iii. e
#se o Brasil ficou entre esses 15 primeiros países, se sim em que posição ficou.

paises = ('Estados Unidos', 'China', 'Japão', 'Grã-Bretanha', 'Comitê russo',
        'Austrália', 'Holanda', 'França', 'Alemanha', 'Itália', 'Canadá',
        'Brasil', 'Nova Zelândia', 'Cuba', 'Hungria')

print(f'Os três primeiros colocados foram: {paises[:3]}')
print(f'Os dois ultimos colocados foram: {paises[13:]}')
if 'Brasil' in str(paises):
    print(f'A posição do Brasil foi: {paises.index("Brasil")+1}º')
else:
    print("O Brasil não está no quadro de medalhas.")
