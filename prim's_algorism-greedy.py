import utility

inf = 1000
w=[[0,  1,  3,inf, inf],
   [1,  0,  3,6,   inf],
   [3,  3,  0,4,   2],
   [inf,6,  4,0,   5],
   [inf,inf,2,5,   0]]


F=set() #선택된 에지 저장
utility.printMatrix(w)
n=len(w)
nearest=n*[0] # vi에 가장 가까운 정점
distance=n*[0] # vi와 nearest[i]를 잇는 이음선의 가중치

for i in range(1,n):
    nearest[i]=0 #vi에서 가장 가까운 정점을 v0으로 초기화
    distance[i]=w[0][i] #v0와 vi을 잇는 이음선의 가중치로 초기화
    
vnear = 0
for j in range(0,n-1):
    minimum = inf
    for i in range(1,n):
        if( 0 <= distance[i] < minimum):
            minimum = distance[i]
            vnear = i

    e = (vnear,nearest[vnear])
    F.add(e)
    distance[vnear] = -1
    
    for i in range(1,n):
        if(w[i][vnear] < distance[i]):
            distance[i] = w[i][vnear]
            nearest[i] = vnear
 
print()
print(F)
