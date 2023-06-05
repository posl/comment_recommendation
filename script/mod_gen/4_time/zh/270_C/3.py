def dfs(i,p):
    global d
    d[i]=p
    for j in g[i]:
        if j==p: continue
        dfs(j,i)
n,x,y=map(int,input().split())
x-=1
y-=1
g=[[] for _ in range(n)]
for _ in range(n-1):
    a,b=map(int,input().split())
    a-=1
    b-=1
    g[a].append(b)
    g[b].append(a)
d=[-1]*n
dfs(x,-1)
ans=[]
while y!=-1:
    ans.append(y)
    y=d[y]
for i in reversed(ans):
    print(i+1,end=" ")
print()

if __name__ == '__main__':
    dfs()