import math

x1 = int(input("Insira um numero inteiro (X1): "))
y1 = int(input("Insira um numero inteiro (Y1): "))
x2 = int(input("Insira um numero inteiro (X2): "))
y2 = int(input("Insira um numero inteiro (Y2): "))

D1 = math.sqrt((x2-x1)**2 + (y2-y1)**2)
if  D1>=10:
    print("longe")
else:
    print("perto")
 
