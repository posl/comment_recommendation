def main():
    n, k = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    def is_ok(x):
        s = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(n):
                s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j]
                if a[i][j] <= x:
                    s[i + 1][j + 1] += 1
        for i in range(n - k + 1):
            for j in range(n - k + 1):
                if s[i + k][j + k] - s[i][j + k] - s[i + k][j] + s[i][j] <= (k * k) // 2:
                    return True
        return False
    ok = 0
    ng = 10 ** 9 + 1
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    print(ok)
