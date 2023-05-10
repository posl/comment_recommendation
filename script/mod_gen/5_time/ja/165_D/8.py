def solve(a,b,n):
    if b <= n:
        x = b - 1
    else:
        x = n
    return (a*x)//b - a*(x//b)

if __name__ == '__main__':
    solve()