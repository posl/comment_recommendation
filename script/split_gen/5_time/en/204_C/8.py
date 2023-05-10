def solve():
    N,M = map(int,input().split())
    if M == 0:
        print(N)
        return
    else:
        ans = 0
        for i in range(1,N+1):
            ans += i
        print(ans)
