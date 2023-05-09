def solve():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    P.sort(key=lambda x: x[0] + x[1] + x[2], reverse=True)
    sum_ = sum(P[K-1])
    for i in range(K):
        if sum_ < sum(P[i]):
            print("No")
        else:
            print("Yes")
