def main():
    N = int(input())
    a = [[0 for i in range(10)] for j in range(N + 1)]
    for i in range(1, 10):
        a[1][i] = 1
    for i in range(2, N + 1):
        for j in range(0, 10):
            if j == 0:
                a[i][j] = a[i - 1][j + 1]
            elif j == 9:
                a[i][j] = a[i - 1][j - 1]
            else:
                a[i][j] = a[i - 1][j - 1] + a[i - 1][j + 1]
    ans = 0
    for i in range(0, 10):
        ans += a[N][i]
    print(ans % 998244353)

if __name__ == '__main__':
    main()