def main():
    n, k = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    b = [[0 for j in range(n + 1)] for i in range(n + 1)]
    for i in range(n):
        for j in range(n):
            b[i + 1][j + 1] = b[i][j + 1] + b[i + 1][j] - b[i][j] + a[i][j]
    def check(x):
        for i in range(n - k + 1):
            for j in range(n - k + 1):
                if b[i + k][j + k] - b[i][j + k] - b[i + k][j] + b[i][j] >= x:
                    return True
        return False
    def solve():
        l = -1
        r = 10 ** 9 + 1
        while r - l > 1:
            m = (l + r) // 2
            if check(m):
                l = m
            else:
                r = m
        return l
    print(solve())

if __name__ == '__main__':
    main()