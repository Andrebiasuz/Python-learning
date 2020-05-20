import math

a = float(input("Digite o valor de entrada A : "))
b = float(input("Digite o valor de entrada B : "))
c = float(input("Digite o valor de entrada C : "))
delta = (b**2 - 4*a*c)
if   delta < 0:
      print ("esta equação não possui raízes reais")
if   delta >= 0 :
     x1 = (b**2 + math.sqrt(delta))/2*a
     if   delta == 0:
          print ("a raiz desta equação é",x1)
     else:
          x2 = (b**2 - math.sqrt(delta))/2*a
          if x2>x1:
              print ("as raízes da equação são",x1," e ",x2)
          else:
              print ("as raízes da equação são",x2,"e",x1)
