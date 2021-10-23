# Crie um dicionário que armazene o nome de um álbum, o artista e o seu ano de lançamento.
# Imprima as informações armazenadas no dicionário.

album = str
artista = str
ano_lancamento = int

streaming = { 'album': input("Insira um album: "), 
              'artista': input("Insira um artista: "), 
              'ano_lancamento': input("Insira o ano de lançamento: ")}

print("o album inserido foi", streaming['album'], "do artista", streaming['artista'], "lançado em", streaming['ano_lancamento'])