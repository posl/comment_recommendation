def solve(x,a,d,n):
    if n == 0:
        return 0
    if a > x:
        return min(a-x,solve(x,a+d,d,n-1))
    else:
        return min(x-a,solve(x,a+d,d,n-1))

if __name__ == '__main__':
    solve()