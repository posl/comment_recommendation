def solve():
    n, m = map(int, input().split())
    print((n*(n-1)+m*(m-1))//2)

if __name__ == '__main__':
    solve()