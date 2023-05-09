def main():
    N, M, Q = map(int, input().split())
    a, b, c, d = [], [], [], []
    for _ in range(Q):
        tmp = list(map(int, input().split()))
        a.append(tmp[0])
        b.append(tmp[1])
        c.append(tmp[2])
        d.append(tmp[3])
    ans = 0
    for i in range(1, M+1):
        A = [i]
        ans = max(ans, dfs(N, M, Q, A, a, b, c, d))
    print(ans)
