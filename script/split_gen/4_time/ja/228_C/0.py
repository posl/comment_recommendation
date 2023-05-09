def solve():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    rank = [0] * N
    for i in range(N):
        rank[i] = sum(P[i])
    rank.sort(reverse=True)
    for i in range(N):
        if rank[i] >= rank[K-1]:
            print("Yes")
        else:
            print("No")
