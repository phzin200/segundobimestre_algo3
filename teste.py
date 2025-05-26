#testando_definicoes.py

compras = {"pao","cafe","leite"}
print(compras[0])

#pode ser removido pelo nome do produto ou pelo indice
compras.remove(compras[0])
print(compras)

#append  acrescenta um item no final da lista, so pode adicionar um por vez
compras.append ("pao")
print(compras)


compras_ordenada = sorted(compras)
print(compras_ordenada)