def main():
    N, M, Q = map(int, input().split())
    a = [0] * Q
    b = [0] * Q
    c = [0] * Q
    d = [0] * Q
    for i in range(Q):
        a[i], b[i], c[i], d[i] = map(int, input().split())
    ans = 0
    for i in range(1, M + 1):
        A = [i]
        ans = max(ans, dfs(N, M, Q, a, b, c, d, A))
    print(ans)

if __name__ == '__main__':
    main()