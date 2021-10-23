#Duas pessoas estão se conhecendo e responderam a seguinte pergunta: “o que você gosta
#de fazer no seu tempo livre?” A resposta de cada uma das pessoas foi armazenada em uma
#lista de lazer. Responda o que se pede:
#a. Quais os lazeres que as pessoas possuem em comum?
#b. O que somente a primeira pessoa gosta de fazer no seu tempo livre?
#c. O que somente a segunda pessoa gosta de fazer no seu tempo livre?
#d. O que as duas pessoas gostam de fazer no seu tempo livre?
lazer = list()

pessoa_dois = str
pessoa_um = str

while True:
    pessoa_um = lazer[input("O que você gosta de fazer no seu tempo livre?")]
    pessoa_dois = lazer[input("O que você gosta de fazer no seu tempo livre?")]

    if lazer[pessoa_um] in lazer[pessoa_dois]:
        print(f'As duas pessoas possuem as seguintes atividades de lazer em comum: {lazer.index[pessoa_um] == lazer.index[pessoa_dois]}')

