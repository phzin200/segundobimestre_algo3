pacotes=("ABC123,XYZ780,DEF456 ,JKL321, MNO654, PQR987 ,STU741")

rastreio=("enviado","recebido","em transito","enviado","recebido","em transito","enviado")

quantidade_enviado=rastreio.count("enviado")
quantidade_recebido=rastreio.count("recebido")
quantidade_em_transito=rastreio.count("em transito")

for i in range (0, len("em transito")):
    if rastreio[i]=="em transito":
        codigos_do_em_transito= codigos_do_em_transito.append(pacotes[i])

pesquisa=input("Insira o código para verificar o status do pacote")
teste=pesquisa in pacotes
if teste!=0:
    for i in range (0,len(pacotes)):
        if pesquisa==pacotes[i]:
            print(rastreio[i])
            