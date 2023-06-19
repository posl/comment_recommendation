def solve(n, s):
    a = [0]*n
    a[0] = s[0]
    for i in range(1, n):
        a[i] = s[i] - s[i-1]
    return a

if __name__ == '__main__':
    solve()