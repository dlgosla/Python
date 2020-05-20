import utility

def Make_table(a,b,m,n):
    table=[[0 for j in range(0,n+1)] for i in range(0,m+1)]   

    for j in range(n-1,-1,-1):#0~9
        table[m][j] =table[m][j+1]+2

    for i in range(m-1,-1,-1):#0~7
        table[i][n] =table[i+1][n]+2


    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):
            penalty = 1
            if(a[i] == b[j]):
                penalty = 0
            table[i][j] = min(table[i+1][j+1]+penalty , table[i+1][j]+2, table[i][j+1]+2)
    return table

def Make_minindex(m,n):
    minindex = [[ (0,0) for j in range(0,n+1)] for i in range(0,m+1)]
    i=0
    j=0
    while(i<m and j<n):
            penalty = 1
            if(a[i] == b[j]):
                penalty = 0
            
            if(table[i][j+1]+2 == table[i][j]):
                minindex[i][j] = (i,j+1)
                j = j + 1
            
            elif(table[i+1][j]+2 == table[i][j]):
                minindex[i][j] = (i+1,j)
                i = i + 1 
            
            elif (table[i+1][j+1] + penalty == table[i][j]):
                minindex[i][j] = (i+1,j+1)
                i= i + 1
                j = j + 1
    return minindex

def Print_opt_path(minindex,m,n):
    x=0
    y=0
    while (x <m and y <n):
        if(minindex[x][y]==(0,0)):
            x=x+1
            y=y+1
            continue
    
        tx, ty = x, y
        print(minindex[x][y])
        (x,y)= minindex[x][y]
    
        if x == tx + 1 and y == ty+1:
            print(a[tx]," ",  b[ty])
        
        elif x == tx and y == ty+1:
            print(" - ", " ", b[ty])
        
        else:
            print(a[tx], " " , " -")
            
a=['A','A','C','A','G','T','T','A','C','C']
b=['T','A','A','G','G','T','C','A']

m=len(a)#10
n=len(b)#8

print("-------------------1번문제-------------------")
table = Make_table(a,b,m,n)
print("table: \n")
utility.printMatrix(table)
minindex = Make_minindex(m,n)
print()
print("최적서열 맞춤: \n")
Print_opt_path(minindex,m,n)
print()
print()
    
a=['T', 'G', 'A', 'C', 'A', 'A', 'G', 'T']
b=['T', 'A', 'C', 'A', 'A', 'T', 'T']

print("----------------2번문제-----------------")
m=len(a)
n=len(b)
table = Make_table(a,b,m,n)
print("table: \n")
utility.printMatrix(table)
minindex = Make_minindex(m,n)
print()
print("최적서열 맞춤: \n")
Print_opt_path(minindex,m,n)

