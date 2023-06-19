def solve():
    N,K = map(int,input().split())
    p = list(map(int,input().split()))
    s = [0]*(N+1)
    for i in range(N):
        s[i+1] = s[i]+p[i]
    ans = 0
    for i in range(N-K+1):
        ans = max(ans,(s[i+K]-s[i])/2+(s[i]+s[i+K])/2/K)
    print(ans)

if __name__ == '__main__':
    solve()