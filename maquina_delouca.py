import time



ligado: False
tempo: 0
temperatura: 0 

def ligar(novo_tempo, novo_grau):
    global ligado, tempo, potencia 
    if not ligado:
        ligado = True
        tempo = novo_tempo
        grau = novo_grau
        print(f' microondas ligado por (tempo)segundos no grau (grau)')
        iniciar_cronometros(tempo)
        desligar() #desligar automaticamente
    else:
        print('a maquina ja esta ligado')
        
def desligar():
     global ligado
     if ligado:
       ligado = False
       print('maquina esta desligado') 
     else:
       print ('maquina esta desligado')
    
def status():
    if ligado:
        print(f' tempo: (tempo)segundos \n temeperatura:(temperatura)')
    else:
        print(f"desligado")
        
def iniciar_cronometros(segundos):
    while segundos>0:
        print(f"tempo restante: {segundos}  segundos",end="\r")
        time.sleep(1)
        segundos -= 1
    print("\n tempo esgotado")
    
def vidro():
    ligar(120,100)
    
vidro()

def plastico():
    ligar(60,21)
    
plastico()

def metal():
    ligar(180,30)
        
metal()