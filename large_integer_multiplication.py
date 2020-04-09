def prod2(a,b):
    n = max(len(str(a)),len(str(b)))
    
    threshold = 4
    
    if(a==0 or b==0):
        return 0
    
    elif(n<= threshold):
        return a*b

    else:
        m = n // 2
        x = a // 10**m
        y = a % 10**m
        w = b // 10**m
        z = b % 10**m
        r = prod2(x+y,w+z)
        p = prod2(x,w)
        q = prod2(y,z)

    return p*pow(10,2*m) + (r-p-q)*10**m + q

    
a=1234567812345678
b=2345678923456789

print(prod2(a,b))
print(a*b)
