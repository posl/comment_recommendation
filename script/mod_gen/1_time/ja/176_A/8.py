def solve():
    n,x,t = map(int, input().split())
    print(-(-n//x)*t)

if __name__ == '__main__':
    solve()