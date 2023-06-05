def main():
    n, k = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    b = [[0]*(n+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(n):
            b[i+1][j+1] = a[i][j] + b[i][j+1] + b[i+1][j] - b[i][j]
    def get(x, y):
        return b[x][y] - b[x-k][y] - b[x][y-k] + b[x-k][y-k]
    def check(x):
        for i in range(n-k+1):
            for j in range(n-k+1):
                if get(i+k, j+k) - get(i+k, j) - get(i, j+k) + get(i, j) >= x:
                    return True
        return False
    def solve():
        l = -1
        r = 10**9 + 1
        while r - l > 1:
            mid = (l + r) // 2
            if check(mid):
                l = mid
            else:
                r = mid
        return l
    print(solve())

if __name__ == '__main__':
    main()