import utility
e={0:[1,2,3], 1:[2,5], 2:[3,4,5,6], 3:[4,6],4:[6,7]}
n=8
a = [ [0 for j in range(0,n)] for i in range(0,n)]
for i in range(0,n-1):
    for j in range(i+1,n):
        if i in e:
           if j in e[i]:
              a[i][j]=1
              a[j][i]=1
utility.printMatrix(a)

visited =n*[0]

def DFS(a,v):
    visited[v] = 1;
    print(v)
    for i in range(8):
        if(visited[i] == 0):
            if(a[v][i] == 1):
                DFS(a,i)
                     
DFS(a,0)
print()
print()

def promising(i,col):
    k = 0
    switch = True
    while k<i and switch:
        if( col[i] == col[k] or abs(col[i]-col[k]) == i-k):
            switch = False
        k = k + 1
    return switch

def queens(n,i,col):
    if(promising(i,col)):
        if(i==n-1):
            print(col)
        else:
            for j in range(0,n):
                col[i+1] = j
                queens(n,i+1,col)


n=5
col=n*[0]
queens(n,-1,col)
