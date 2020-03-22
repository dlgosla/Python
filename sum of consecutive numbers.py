import random
import sys

while(True):
    print("---------------------------------------\n")
    n = input("리스트의 길이를 입력하세요: ")
    n = int(n)
    if( n < 3):
        print("3 이상의 수를 입력하세요.")
        continue
    break

S = [0]*n

for i in range(0,n):
    S[i] = random.randrange(1,11)

while(True):
    m = input("연속한 정수를 몇개씩 더하시겠습니까?")
    m = int(m)

    if m > n :
        print("\n리스트의 길이보다 큽니다\n")
        continue
    
    if m == 0:
        sys.exit()

    listA = []
    
    for i in range(0,n):
        sum = 0
        
        if(i+m > n):
            break
        
        for j in range(i,i+m):
            sum += S[j]
        listA.append(sum)

    print("\n현재 랜덤하게 생성된 변수 리스트: ",S)
    print("연속된",m,"개의 변수의 합 리스트",listA,"\n")
   
    
    listA.sort()
    tmin = listA[0]
    tmax = listA.pop()
    
    print("연속한 m개의 정수의 합 중 제일 큰 값: ",tmax)
    print("연속한 m개의 정수의 합 중 가장 작은  값: ",tmin,"\n")
    print("---------------------------------------\n")
    

    


