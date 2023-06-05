def solve(n, m, a):
    a.sort(reverse=True)
    for i in range(m):
        a[0] //= 2
        a.sort(reverse=True)
    return sum(a)

if __name__ == '__main__':
    solve()