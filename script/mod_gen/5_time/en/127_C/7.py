def solve():
    n,m = map(int,input().split())
    l = 0
    r = n
    for _ in range(m):
        x,y = map(int,input().split())
        l = max(l,x)
        r = min(r,y)
    print(max(r-l+1, 0))
solve()

if __name__ == '__main__':
    solve()