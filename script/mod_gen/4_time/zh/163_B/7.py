def solve():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    if sum(a) > n:
        print(-1)
    else:
        print(n-sum(a))

if __name__ == '__main__':
    solve()