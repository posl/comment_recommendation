def solve():
    N,K = map(int,input().split())
    ans = 0
    for i in range(1,N+1):
        tmp = 1
        while i < K:
            i *= 2
            tmp *= 0.5
        ans += tmp
    print(ans/N)

if __name__ == '__main__':
    solve()