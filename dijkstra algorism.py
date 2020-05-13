inf=1000
w=[[0,7,4,6,1],[inf,0,inf,inf,inf],
   [inf,2,0,5,inf], [inf,3,inf,0,inf], [inf,inf,inf,1,0]]
n=5
f=set()
touch=n*[0]
length=n*[0]


for i in range(1,n):
    length[i] = w[0][i]
    touch[i] = 0

vnear = 0
for i in range(1,n):
    minimum = inf
    for j in range(1,n):
        if( 0 <= length[j] and length[j] < minimum):
            minimum = length[j]
            vnear = j

    e = (touch[vnear], vnear)
    f.add(e)

    for j in range(1,n):
        if(length[vnear] + w[vnear][j] < length[j]):
            length[j] = length[vnear] + w[vnear][j]
            touch[j] = vnear
    length[vnear] = -1

print(f)


inf=1000
w=[[0,7,4,6,1],[inf,0,inf,inf,inf],
   [inf,2,0,5,inf], [inf,3,inf,0,inf], [inf,inf,inf,1,0]]
n=5
f=set()
touch=n*[0]
length=n*[0]
save_length=n*[0]


#구현

print(save_length) 

