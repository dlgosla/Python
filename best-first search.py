import queue

class Node:
        def __init__(self,level=0,weight=0, profit=0, bound=0.0, include=[]):
                self.level = level
                self.weight = weight
                self.profit = profit
                self.bound = bound
                self.include = include
        def __cmp__(self, other):
               return cmp(self.bound, other.bound)

def kp_Best_FS():
        global maxProfit
        global bestset
        temp = n*[0]
        maxProfit = 0
        PQ = queue.Queue()
        v1 = Node(-1,0,0, 0.0,temp) # T의 루트
        v1.bound = compBound(v1)
        PQ.put(v1)
        
        while not(PQ.empty()):
            maxBound = -1000000
            nodeList  = []
            for i in range(PQ.qsize()):
                nodeList.append(PQ.get())

            for i in range(len(nodeList)):
                if(nodeList[i].bound > maxBound):
                    maxBound = nodeList[i].bound
                    index = i

            v = nodeList[i]
            nodeList.pop(i)
    
            for i in range(len(nodeList)):
                PQ.put(nodeList[i])

            if( v.bound > maxProfit): #마디가 아직 유망한 지 확인
                u = Node(0,0,0, 0.0,v.include[:]) #자식노드
                u.level = v.level + 1
                u.weight = v.weight + w[u.level]
                u.profit = v.profit + p[u.level]
                
                if (u.weight <= W) and (u.profit > maxProfit): #지금까지 제일 좋은 것이면
                    u.include.pop(u.level)
                    u.include.insert(u.level, 1)
                    maxProfit = u.profit #maxProfit 갱신
                
                u.bound = compBound(u) #바운드 계산
                if(u.bound > maxProfit): #유망하면
                    bestset = u.include
                    PQ.put(u) #PQ에 넣음
                
                u1 = Node(-1,0,0, 0.0,v.include[:])
                u1.level = v.level +1
                u1.weight = v.weight   
                u1.profit = v.profit
                u1.bound = compBound(u1)      #이 자식노드를 경로에 안넣었을 경우 바운드 계산
                u1.include.pop(u1.level)
                u1.include.insert(u1.level, 0)
                if(u1.bound > maxProfit): #유망하면
                    bestset = u1.include
                    PQ.put(u1) #PQ에 집어넣음
               
            
def compBound(u):
        if u.weight >=W:
            return 0
        else:
            result = u.profit
            j = u.level + 1
            totweight = u.weight

            while ( j< n and totweight + w[j] <= W):
                totweight += w[j]
                result = result + p[j]
                j += 1
                
            k = j
            if k < n:
                result = result + (W-totweight) * p[k]/w[k]
            return result

# heap이 minheap이라 bound를 계산하여 -를 하여 리턴한다. 비교를 < maxProfit으로 수행한다.
n=4
W=16
p=[40,30,50,10]
w=[2,5,10,5]
include=[0]*n
maxProfit =0
bestset=n*[0]
kp_Best_FS()
print(bestset)
print(maxProfit)

