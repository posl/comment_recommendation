def solve(n, a):
    if n == 1 and a[0] == 1:
        return 0
    if n == 1 and a[0] != 1:
        return -1
    if n > 1 and a[0] != 1:
        return -1
    if n > 1 and a[0] == 1:
        for i in range(1, n):
            if a[i] - a[i-1] != 1:
                return i
        return n - 1

if __name__ == '__main__':
    solve()