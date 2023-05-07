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
    for i in range(1, M + 1):
        ans = max(ans, dfs(1, [i], N, M, Q, a, b, c, d))
    print(ans)
