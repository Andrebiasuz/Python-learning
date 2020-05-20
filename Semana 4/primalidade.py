k = 0
p = True
i = 0
t = 0
n = int(input("Digite o valor de n:"))
while(i<=n):
    if (i>1):
        t= float(n%i)
        k= n//i
        if (t==0 and k!=1):
            p = False
    i=i+1
if(p==False):
    print("Não Primo")
else:
        print("Primo")
