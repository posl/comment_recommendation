def solve(n, a):
    if n % 2 == 0:
        return sum(a)
    else:
        return sum(a) - 2 * min(abs(a[i]) for i in range(n))

if __name__ == '__main__':
    solve()