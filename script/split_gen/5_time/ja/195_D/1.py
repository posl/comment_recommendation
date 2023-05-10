def solve():
    N, M, Q = map(int, input().split())
    W = [0] * N
    V = [0] * N
    for i in range(N):
        W[i], V[i] = map(int, input().split())
    X = list(map(int, input().split()))
    queries = [list(map(int, input().split())) for _ in range(Q)]
    for L, R in queries:
        boxes = X[:L-1] + X[R:]
        boxes.sort()
        used = [False] * N
        ans = 0
        for b in boxes:
            max_v = 0
            max_i = -1
            for i in range(N):
                if not used[i] and W[i] <= b and max_v < V[i]:
                    max_v = V[i]
                    max_i = i
            if max_i >= 0:
                used[max_i] = True
                ans += max_v
        print(ans)
