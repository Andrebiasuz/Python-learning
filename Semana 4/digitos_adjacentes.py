teste = False
i = 1
n = int(input("Digite um numero inteiro para análise : "))
l = len(str(n))
if (l>=2):
    while (i<=l and teste==False):
        n1 = n%10
        n2 = n//10
        n3 = n2%10
        if (n1==n3):
            teste = True
            print("Sim")
        n=n2
        i = i+1
if(teste==False):
        print("Não")
