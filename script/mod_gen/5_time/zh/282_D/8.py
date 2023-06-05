def solve():
    n, m = map(int, input().split())
    u = [0] * m
    v = [0] * m
    for i in range(m):
        u[i], v[i] = map(int, input().split())
    print(n * (n - 1) // 2 - m)
    return 0

if __name__ == '__main__':
    solve()