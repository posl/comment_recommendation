def solve():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    Q = [0] * N
    for i in range(N):
        Q[P[i] - 1] = i + 1
    #print("Q:", Q)
    for i in range(K - 1, N):
        print(Q[i])
