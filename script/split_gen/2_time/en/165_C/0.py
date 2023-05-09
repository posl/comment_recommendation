def main():
    N, M, Q = map(int, input().split())
    a = [0] * Q
    b = [0] * Q
    c = [0] * Q
    d = [0] * Q
    for i in range(Q):
        a[i], b[i], c[i], d[i] = map(int, input().split())
        a[i] -= 1
        b[i] -= 1
    ans = 0
    A = [0] * N
    def dfs(x):
        global ans
        if x == N:
            score = 0
            for i in range(Q):
                if A[b[i]] - A[a[i]] == c[i]:
                    score += d[i]
            ans = max(ans, score)
            return
        for i in range(A[x - 1], M + 1):
            A[x] = i
            dfs(x + 1)
    dfs(0)
    print(ans)
