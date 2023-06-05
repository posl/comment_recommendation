def solve(n,x,y):
    if n==1:
        return 0
    else:
        return (n-1)*min(x,y)+solve(n-1,x,y)

if __name__ == '__main__':
    solve()