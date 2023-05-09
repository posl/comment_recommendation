def main():
    n, m, q = map(int, input().split())
    a = []
    b = []
    c = []
    d = []
    for _ in range(q):
        ai, bi, ci, di = map(int, input().split())
        a.append(ai)
        b.append(bi)
        c.append(ci)
        d.append(di)
    ans = 0
    def dfs(s, A):
        global ans
        if len(A) == n:
            score = 0
            for i in range(q):
                if A[b[i] - 1] - A[a[i] - 1] == c[i]:
                    score += d[i]
            ans = max(ans, score)
            return
        for i in range(s, m + 1):
            A.append(i)
            dfs(i, A)
            A.pop()
    dfs(1, [])
    print(ans)
