def solve(n):
    if n==1:
        return 0
    elif n==2:
        return 2
    else:
        return (10**n-2*9**n+8**n)%(10**9+7)

if __name__ == '__main__':
    solve()