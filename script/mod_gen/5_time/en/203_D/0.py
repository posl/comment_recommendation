def solve():
    n, k = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    b = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(n):
            b[i + 1][j + 1] = b[i + 1][j] + b[i][j + 1] - b[i][j] + a[i][j]
    def check(x):
        for i in range(n - k + 1):
            for j in range(n - k + 1):
                if b[i + k][j + k] - b[i][j + k] - b[i + k][j] + b[i][j] >= x:
                    return True
        return False
    l, r = 0, 10 ** 9 + 1
    while r - l > 1:
        m = (l + r) // 2
        if check(m):
            l = m
        else:
            r = m
    print(l)
solve()

if __name__ == '__main__':
    solve()