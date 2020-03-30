import random

def alg1(A):
    Max = [0]*(n)
    Max[0] = A[0]

    for i in range(1,n+1):
        for j in range(0,i):
            if(Max[j] < A[j]):
                Max[i-1] = A[j]
                print(Max)
                
    return Max
            

def alg2(A):
    Max = [0]*n
    for i in range(0,n):
        M
    return alg2(A)
        


n = input("리스트 A의 원소의 개수를 입력하세요: ")
n = int(n)
A = list()

for i in range(0,n):
    A.append(random.randrange(1,100))

print("리스트 A의 원소:", A)

print(alg1(A))
print(alg2(A))
