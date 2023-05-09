def main():
    n, m, q = map(int, input().split())
    a = [0] * q
    b = [0] * q
    c = [0] * q
    d = [0] * q
    for i in range(q):
        a[i], b[i], c[i], d[i] = map(int, input().split())
        a[i] -= 1
        b[i] -= 1
    ans = 0
    A = [0] * n
    def dfs(i, A):
        nonlocal ans
        if i == n:
            now = 0
            for j in range(q):
                if A[b[j]] - A[a[j]] == c[j]:
                    now += d[j]
            ans = max(ans, now)
            return
        A[i] = A[i-1]
        while A[i] <= m:
            dfs(i+1, A)
            A[i] += 1
    dfs(0, A)
    print(ans)
