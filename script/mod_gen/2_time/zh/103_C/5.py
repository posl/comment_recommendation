def solve(n, a):
    max_a = max(a)
    m = max_a - 1
    while True:
        m += 1
        s = 0
        for i in range(n):
            s += m % a[i]
        if s > max_a:
            break
    return m

if __name__ == '__main__':
    solve()