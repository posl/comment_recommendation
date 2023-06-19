def main():
    n, m = map(int, input().split())
    b = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            b[i][j] -= i * 7
    a = [[(i - 1) * 7 + j + 1 for j in range(7)] for i in range(1, n + 1)]
    for i in range(n):
        for j in range(m):
            a[i][j] -= i * 7
    for i in range(n - 1):
        for j in range(m - 1):
            if b[i][j] != a[i][j]:
                print('No')
                return
    print('Yes')

if __name__ == '__main__':
    main()