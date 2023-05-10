def solve(n, l):
    return sum(l) - min(l, key=abs)

if __name__ == '__main__':
    solve()