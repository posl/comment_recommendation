def solve(n, l):
    return sum(l) - min(l, key=abs)*2

if __name__ == '__main__':
    solve()