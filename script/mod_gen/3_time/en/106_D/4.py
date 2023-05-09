def main():
    n, m, q = map(int, input().split())
    train = [[0] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        l, r = map(int, input().split())
        train[l][r] += 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            train[i][j] += train[i][j - 1]
    for _ in range(q):
        p, q = map(int, input().split())
        ans = 0
        for i in range(p, q + 1):
            ans += train[i][q] - train[i][p - 1]
        print(ans)

if __name__ == '__main__':
    main()