def solve(n, m, a):
    a.sort()
    for i in range(m):
        a[-1] = a[-1] // 2
        a.sort()
    return sum(a)

if __name__ == '__main__':
    solve()