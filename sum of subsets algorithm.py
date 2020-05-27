def promising(i,weight, total):
    return (weight + total >= W) and (weight == W or weight + w[i+1] <= W)
    
def sum_of_subsets(i, weight, total, include):
    if(promising(i,weight,total)): #유망성 판단
        if(weight == W): #전체 무게와 현재까지 포함된 무게가 같으면
            print("sol",include) #정답을 출력
        else:
            include[i+1] = 1 #i+1번째 아이템을 포함할 경우
            sum_of_subsets(i+1, weight+w[i+1], total - w[i+1], include)
            include[i+1] = 0 #i+1번 째 아이템을 포함하지 않을경우
            sum_of_subsets(i+1, weight, total - w[i+1], include)

n=4
w=[1,4,2,6]

W=6
print("items =",w, "W =", W)
include = n*[0]
total=0
for k in w:
    total+=k
sum_of_subsets(-1,0,total,include)
