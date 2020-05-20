def maior_primo(goal):
    count = 2
    k = 0
    p = True
    i = 0
    t = 0
    n = 2
    max_primo = 0

    while (count<=goal):
        while(i<=n):
            if (i>1):
                t= float(n%i)
                k= n//i
                if (t==0 and k!=1):
                    p = False
            i=i+1
        if(p==True):
            max_primo = n
        n=n+1
        i=0
        count = count + 1
        p= True

    return max_primo



    


