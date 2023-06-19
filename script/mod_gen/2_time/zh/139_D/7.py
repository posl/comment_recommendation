def solve(n):
    if n==1:
        return 0
    else:
        return n*(n-1)//2

if __name__ == '__main__':
    solve()