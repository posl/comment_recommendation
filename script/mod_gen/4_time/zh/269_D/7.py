def dfs(v):
    seen[v]=True
    for i in range(len(G[v])):
        if seen[G[v][i]]==False:
            dfs(G[v][i])
            
N=int(input())
X=[0]*N
Y=[0]*N
for i in range(N):
    X[i],Y[i]=map(int,input().split())
    
G=[[] for i in range(N)]
for i in range(N):
    for j in range(i+1,N):
        if X[i]-X[j]==1 and Y[i]-Y[j]==0:
            G[i].append(j)
            G[j].append(i)
        if X[i]-X[j]==0 and Y[i]-Y[j]==1:
            G[i].append(j)
            G[j].append(i)
        if X[i]-X[j]==-1 and Y[i]-Y[j]==1:
            G[i].append(j)
            G[j].append(i)
        if X[i]-X[j]==1 and Y[i]-Y[j]==-1:
            G[i].append(j)
            G[j].append(i)
        if X[i]-X[j]==0 and Y[i]-Y[j]==-1:
            G[i].append(j)
            G[j].append(i)
        if X[i]-X[j]==-1 and Y[i]-Y[j]==0:
            G[i].append(j)
            G[j].append(i)
seen=[False]*N
ans=0
for i in range(N):
    if seen[i]==False:
        dfs(i)
        ans+=1
print(ans)

if __name__ == '__main__':
    dfs()