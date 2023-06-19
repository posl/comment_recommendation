def dfs(x):
    for i in range(len(tree[x])):
        dfs(tree[x][i])
        c[x] += c[tree[x][i]]
n,q = map(int,input().split())
tree = [[] for _ in range(n)]
c = [0]*n
for i in range(n-1):
    a,b = map(int,input().split())
    tree[a-1].append(b-1)
for i in range(q):
    p,x = map(int,input().split())
    c[p-1] += x
dfs(0)
print(*c)

if __name__ == '__main__':
    dfs()