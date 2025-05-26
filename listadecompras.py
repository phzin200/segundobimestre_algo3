compras = []
resposta =(str(input("deseja adcionar item:")))
while resposta == "sim":
    add = (str(input("adiciona comida")))
    compras.append(add)
    print(compras)
    resposta =(str(input("deseja adcionar item:")))
    if  resposta =="sim":
        add2= (str(input("adicionar item")))
        compras.append(add2)
        print(compras)
    else:
        remove=(str(input("remova item")))
        compras.remove(remove)
        print(compras)
