#jogo Nim
# n = pecas no tabuleiro
# m = valor maximo para tirar
# v = inicializacao
# t = auxiliar para laco while


def partida():
    while True:
        
        s= 0 
        n= int(input("Quantas pecas?"))
        m= int(input("Limite de pecas por jogada?"))
        if (n%(m+1) ==0):
            break
            s==1
            print ("Voce comeca!")
            usuario_escolhe_jogada(n,m)
        else:
            break
            s==2
            print ("Computador comeca!")
            computador_escolhe_jogada(n,m)
    if (s==1):
        n=usuario_escolhe_jogada(n,m)
        computador_escolhe_jogada(n,m)
        
    if (s==2):
        usuario_escolhe_jogada(n,m)

    
def usuario_escolhe_jogada(n,m):
    y=int(input("Quantas pecas voce vai tirar?"))
    if (y<=m and y>0):
        if (y==1):
            print("Voce tirou",y,"peca")
        else:
            print("Voce tirou",y,"pecas")
        return y
        partida()
    else:
        print("Oops! Jogada inválida! Tente de novo")

def computador_escolhe_jogada(n,m):
    if (n//(m+1)<1):
        y=n
    else:
        y=(n%(m+1))
    if (y==1):
        print("O computador tirou uma peca")
    elif (y>1):
        print("O computador tirou",y,"pecas")
    return y
    
    


i=0
while (i!=1 and i!=2):
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("")
    print("1 - para jogar uma partida isolada")
    i=int(input("2 - para jogar um campeonato"))
    

if (i==1):
    print("Voce escolheu uma partida!")
    partida()

if (i==2):
    print("Voce escolheu um campeonato!")
















    
