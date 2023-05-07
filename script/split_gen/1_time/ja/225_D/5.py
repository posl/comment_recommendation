def main():
    N,Q = map(int,input().split())
    parent = [-1] * (N+1)
    rank = [0] * (N+1)
    for i in range(Q):
        q = list(map(int,input().split()))
        if q[0] == 1:
            unite(q[1],q[2],parent,rank)
        elif q[0] == 2:
            root1 = find(q[1],parent)
            root2 = find(q[2],parent)
            if root1 != root2:
                if rank[root1] < rank[root2]:
                    parent[root1] = root2
                else:
                    parent[root2] = root1
                    if rank[root1] == rank[root2]:
                        rank[root1] += 1
        else:
            ans = []
            for j in range(1,N+1):
                if find(j,parent) == find(q[1],parent):
                    ans.append(j)
            print(len(ans),*ans)
