def solve(n, m, a, c):
    b = [None] * (m + 1)
    b[m] = c[n + m] // a[n]
    for i in range(m - 1, -1, -1):
        b[i] = (c[n + i] - a[n] * b[m]) // a[i]
    return b
n, m = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))
b = solve(n, m, a, c)
print(*b)

if __name__ == '__main__':
    solve()