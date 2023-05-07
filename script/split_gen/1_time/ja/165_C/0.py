def main():
    n, m, q = map(int, input().split())
    a = [0] * q
    b = [0] * q
    c = [0] * q
    d = [0] * q
    for i in range(q):
        a[i], b[i], c[i], d[i] = map(int, input().split())
    ans = 0
    def dfs(A):
        if len(A) == n:
            s = 0
            for i in range(q):
                if A[b[i] - 1] - A[a[i] - 1] == c[i]:
                    s += d[i]
            nonlocal ans
            ans = max(ans, s)
            return
        if len(A) == 0:
            for i in range(1, m + 1):
                A.append(i)
                dfs(A)
                A.pop()
        else:
            for i in range(A[-1], m + 1):
                A.append(i)
                dfs(A)
                A.pop()
    dfs([])
    print(ans)
