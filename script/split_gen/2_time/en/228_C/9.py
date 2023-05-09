def main():
    N,K = map(int,input().split())
    P = [list(map(int,input().split())) for _ in range(N)]
    total = [0]*N
    for i in range(N):
        total[i] = sum(P[i])
    
    rank = [0]*N
    for i in range(N):
        rank[i] = sum([total[j]>total[i] for j in range(N)])+1
    for i in range(N):
        if rank[i]<=K:
            print('Yes')
        else:
            print('No')
