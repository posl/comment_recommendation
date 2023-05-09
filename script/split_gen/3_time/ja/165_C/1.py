def solve():
    N, M, Q = map(int, input().split())
    a = [0] * Q
    b = [0] * Q
    c = [0] * Q
    d = [0] * Q
    for i in range(Q):
        a[i], b[i], c[i], d[i] = map(int, input().split())
    ans = 0
    def dfs(A):
        global ans
        if len(A) == N:
            score = 0
            for i in range(Q):
                if A[b[i] - 1] - A[a[i] - 1] == c[i]:
                    score += d[i]
            ans = max(ans, score)
            return
        if len(A) == 0:
            for i in range(1, M + 1):
                A.append(i)
                dfs(A)
                A.pop()
        else:
            for i in range(A[-1], M + 1):
                A.append(i)
                dfs(A)
                A.pop()
    dfs([])
    print(ans)
