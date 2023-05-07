def solve():
    N, M, Q = map(int, input().split())
    a = []
    b = []
    c = []
    d = []
    for i in range(Q):
        a_i, b_i, c_i, d_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
        c.append(c_i)
        d.append(d_i)
    A = [0] * N
    ans = 0
    def dfs(i, A_i):
        if i == N:
            score = 0
            for j in range(Q):
                if A[b[j] - 1] - A[a[j] - 1] == c[j]:
                    score += d[j]
            global ans
            ans = max(ans, score)
            return
        for j in range(A_i, M + 1):
            A[i] = j
            dfs(i + 1, j)
    dfs(0, 1)
    print(ans)
