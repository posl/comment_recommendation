def solve():
    N, M, Q = map(int, input().split())
    A = [0 for i in range(N)]
    ans = 0
    for i in range(Q):
        a, b, c, d = map(int, input().split())
        for j in range(a-1, b):
            A[j] = c
        score = 0
        for j in range(N-1):
            if A[j+1] - A[j] == d:
                score += d
        ans = max(ans, score)
    print(ans)
