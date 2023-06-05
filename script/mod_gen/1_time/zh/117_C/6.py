def solve(n,m,x):
    x.sort()
    if n == 1:
        return 0
    if n == 2:
        return x[1]-x[0]
    if n == 3:
        return x[2]-x[0]
    return x[n-1]-x[0]

if __name__ == '__main__':
    solve()