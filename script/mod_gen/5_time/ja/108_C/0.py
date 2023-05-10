def solve():
    N,K = map(int,input().split())
    ans = 0
    if K%2==0:
        for i in range(1,N+1):
            if i%K==0:
                ans += N//K
            elif i%K==K//2:
                ans += N//K
        print(ans**3)
    else:
        for i in range(1,N+1):
            if i%K==0:
                ans += N//K
        print(ans**3)

if __name__ == '__main__':
    solve()