
parent = dict()
rank = dict()

def make_singleton_set(v):
    parent[v] = v
    rank[v] = 1

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]


def union(r1, r2):
    if r1 != r2:
        if rank[r1] > rank[r2]:
            parent[r2] = r1
            rank[r1] += rank[r2]
        else:
            parent[r1] = r2
            if rank[r1] == rank[r2]: rank[r2] += rank[r1]

def kruskal(graph):
    v = list(graph['vertices'])
    edge = list(graph['edges'])
    
    for i in range( 0, len(edge)-1 ):
        for j in range( 0,len(edge)-1):
            if( edge[j][0] >= edge[j+1][0]):
                temp = edge[j]
                edge[j] = edge[j+1]
                edge[j+1] = temp
                
    for i in range(0,len(v)):
        make_singleton_set(graph['vertices'][i])
    
    index = 0
    F = set()
    while(len(F) < len(v) -1):
        e = edge[index]
        (i, j) = (e[1], e[2])
        p = find(i)
        q = find(j)

        if(p != q):
            union(p, q)
            F.add(e)
        index = index + 1
        
    return F

graph = {
        'vertices': ['A', 'B', 'C', 'D', 'E'],
        'edges': set([
            (1, 'A', 'B'),
            (3, 'A', 'C'),
            (3, 'B', 'C'),
            (6, 'B', 'D'),
            (4, 'C', 'D'),
            (2, 'C', 'E'),
            (5, 'D', 'E'),
            ])
        }
mst = kruskal(graph)
print(mst)
