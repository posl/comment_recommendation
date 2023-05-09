def solve(n, a):
    if n == 2:
        if a[0] == a[1]:
            return -1
        else:
            return a[0] + a[1]
    a.sort()
    if a[-1] % 2 == 0:
        return a[-1]
    else:
        a[-1] -= 1
        return a[-1] + a[-2]

if __name__ == '__main__':
    solve()