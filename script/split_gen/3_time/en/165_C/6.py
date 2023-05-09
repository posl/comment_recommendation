def solve():
    N, M, Q = map(int, input().split())
    A = [0] * Q
    for i in range(Q):
        A[i] = list(map(int, input().split()))
    ans = 0
    def dfs(cur, last):
        nonlocal ans
        if cur == N:
            score = 0
            for a, b, c, d in A:
                if A[b - 1] - A[a - 1] == c:
                    score += d
            ans = max(ans, score)
            return
        for i in range(last, M + 1):
            A[cur] = i
            dfs(cur + 1, i)
    dfs(0, 1)
    print(ans)
