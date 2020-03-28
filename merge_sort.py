def mergeSort(n, s):
    h = n // 2
    m = n - h
    
    u = [0]*h
    v = [0]*m

    
    if(n > 1):
        for i in range(0,h):
            u[i] = s[i]

        for i in range(0,m):
            v[i] = s[h+i]

        mergeSort(h,u)
        mergeSort(m,v)
        merge(h,m,u,v,s)
        

                

def merge(h,m,u,v,s):
    i = 0
    j = 0
    k = 0

    while( i < h and j < m):
        if(u[i] < v[j]):
           s[k] = u [i]
           i=i+1
           
        else:
           s[k] = v[j]
           j=j+1
           
        k=k+1
        

    if (i >= h):
        for index in range(j,m):
            s[k] = v[index]
            k=k+1
       
    elif(j >= m):
        for index in range(i,h):
            s[k] = u[index]
            k=k+1

         
s=[3,5,2,9,10,14,4,8]
mergeSort(8,s)
print(s) 
