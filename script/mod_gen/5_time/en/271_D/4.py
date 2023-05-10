def solve(n, s, a):
    for i in range(2 ** n):
        sum = 0
        for j in range(n):
            if (i >> j) & 1:
                sum += a[j][0]
            else:
                sum += a[j][1]
        if sum == s:
            return True, i
    return False, 0
n, s = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
result, ans = solve(n, s, a)

if __name__ == '__main__':
    solve()