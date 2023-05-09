def solve():
    n, m = map(int, input().split())
    x = [int(i) for i in input().split()]
    c = [0] * n
    y = [0] * n
    for i in range(m):
        c[i], y[i] = map(int, input().split())
    c = c[:m]
    y = y[:m]
    ans = 0
    for i in range(n):
        ans += x[i]
    for i in range(n - 1):
        if c[i] == c[i + 1]:
            y[i + 1] = 0
    for i in range(n):
        ans += y[i]
    print(ans)

if __name__ == '__main__':
    solve()