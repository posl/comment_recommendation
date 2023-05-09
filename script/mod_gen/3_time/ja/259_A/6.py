def solve(n, m, x, t, d):
    for i in range(x):
        t -= d
    for i in range(x, m):
        t += d
    return t
n, m, x, t, d = map(int, input().split())
print(solve(n, m, x, t, d))

if __name__ == '__main__':
    solve()