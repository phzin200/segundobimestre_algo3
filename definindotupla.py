numero = (5, 8, 12, 8, 7, 8, 3)
#para ser uma tupla precisa estar entre parênteses!!!!
print("tupla original:", numero)
#imprimindo para o usuario a tupla original, sem manipulações!
print("tamanho da tupla:", len(numero))
print(numero[2])
print("fazendo um slicing do 2 ao 5", numero[2:5])
#o slicing ele não pega o último item definido no recorte.
print("quantas vezes o numero 8 repete", numero.count (8))
print("posição da primeira ocorrecia do numero 7:", numero.index(7))
minimo_tupla=min(numero)
print(minimo_tupla)
maximo_tupla=max(numero)
print(maximo_tupla)
soma_tupla=sum(numero)
print(soma_tupla)
organizar_tupla=sorted(numero)
print(organizar_tupla)
print("o numero 4 esta na tupla???", 4 in numero)
numero2=(15,20)
tupla_concatenada=numero+numero2
print("a conceatenacao das tupla 1 e 2 resulta na nova tupla:",tupla_concatenada)
tupla_duplicada=numero*2
print(tupla_duplicada)

