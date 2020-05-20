#2018110654 이해님

import numpy

def bin1(n,k):
    if(k==0 or n ==k):
        return 1;
    else:
        return bin1(n-1,k-1) + bin1(n-1,k)


def bin2(n,k):
    b = numpy.array(range((n+1)*(k+1))).reshape((n+1,k+1))
    for i in range(0,n+1):
        for j in range(0,min(i,k)+1):
            if(j==0 or j==i):
                b[i][j] = 1
                
            else:
                b[i][j] = b[i-1][j-1] + b[i-1][j]
                
    return b[n][k]

                       

def allShortestPath(g,n):
    p = numpy.array(range(n*n)).reshape((n,n))               
    for i in range(0,n):          
        for j in range(0,n):
            p[i][j] = 0
    d=g

    for k in range(0,n):
        for i in range (0,n):
            for j in range(0,n):
                if(d[i][k] + d[k][j] < d[i][j]):
                    p[i][j] = k+1;
                    d[i][j] = d[i][k] + d[k][j]
    return d,p

def path2(q, r,count):
    if(count == 0):
        q=q-1
        r=r-1
    
    if (p[q][r] != 0):
        count = count+1
        path2(q , p[q][r]-1, count)
        print(" v", p[q][r])
        path2(p[q][r]-1 , r , count)

def printMatrix(d):
    n=len(d[0])
    for i in range(0,n):
        for j in range(0,n):
            print(d[i][j],end=" ")
        print()


inf=1000
g=[[0,1,inf, 1,5],
   [9,0,3,2,inf],
   [inf,inf,0,4,inf],
   [inf,inf,2,0,3],
   [3,inf,inf,inf,0]]

print()
printMatrix(g)

d, p = allShortestPath(g,5)
print()
printMatrix(d)
print()
printMatrix(p)
print()

count = 0
path2(5,3,count)
print()


print("bin(10,5): " ,bin1(10,5))
print("bin2(10,5): ",bin2(10,5))
