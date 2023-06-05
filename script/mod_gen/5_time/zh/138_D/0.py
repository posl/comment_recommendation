def dfs(now,par):
    for i in range(len(tree[now])):
        if tree[now][i] != par:
            dfs(tree[now][i],now)
            count[now] += count[tree[now][i]]
    return
N,Q = map(int,input().split())
tree = [[] for i in range(N)]
for i in range(N-1):
    a,b = map(int,input().split())
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)
count = [0]*N
for i in range(Q):
    p,x = map(int,input().split())
    count[p-1] += x
dfs(0,-1)
for i in count:
    print(i,end=" ")
print()

if __name__ == '__main__':
    dfs()