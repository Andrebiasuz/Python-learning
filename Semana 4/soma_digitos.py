i = 0
j = 0
t = 0
soma = 0

n = int(input("Digite o valor de n: "))
i = n
l = len(str(n))
while (t<=l):
        j = i//10
        i = i%10
        soma = i + soma
        i = j
        t = t+1
        
print(soma)
