def fizzbuzz(n):
    i = 0
    if  (n%3==0):
        z=str("Fizz")
        i = 1
    if (n%5==0):
        if i==1:
            z=str("FizzBuzz")
        else:
            z=str("Buzz")
            i = 2
        
    if (i==0):
        z=int(n)
    return z
        
    


    

