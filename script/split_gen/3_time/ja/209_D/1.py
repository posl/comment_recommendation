def main():
    N,Q=map(int,input().split())
    G=[[] for i in range(N+1)]
    for i in range(N-1):
        a,b=map(int,input().split())
        G[a].append(b)
        G[b].append(a)
    #print(G)
    #print(N,Q)
    #p
