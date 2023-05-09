def main():
    N,X,Y=map(int,input().split())
    X-=1
    Y-=1
    G=[[] for _ in range(N)]
    for _ in range(N-1):
        u,v=map(int,input().split())
        u-=1
        v-=1
        G[u].append(v)
        G[v].append(u)
    d=[-1]*N
    d[X]=0
    q=[X]
    while q:
        v=q.pop()
        for w in G[v]:
            if d[w]!=-1:continue
            d[w]=d[v]+1
            q.append(w)
    for i in range(N):
        if i==X:continue
        if d[i]==d[Y]//2:
            print(i+1)
            return
    print(Y+1)
main()
