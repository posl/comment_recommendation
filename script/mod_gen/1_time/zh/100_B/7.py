def solve():
    d, n = map(int, input().split())
    print((100**d)*n if n < 100 else (100**d)*(n+1))

if __name__ == '__main__':
    solve()