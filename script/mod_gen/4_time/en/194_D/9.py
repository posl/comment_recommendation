def solve(n):
    return sum([i*(1/n) for i in range(1,n+1)])

if __name__ == '__main__':
    solve()