def solve(n, a):
    if n == 1:
        return a[0]
    elif n == 2:
        return a[0] ^ a[1]
    else:
        return 0

if __name__ == '__main__':
    solve()