def main():
    N,K = map(int,input().split())
    p = list(map(int,input().split()))
    #i番目のサイコロを振った時の期待値
    e = [0 for _ in range(N)]
    for i in range(N):
        e[i] = (p[i]+1)/2
    #print(e)
    #累積和
    s = [0 for _ in range(N+1)]
    for i in range(N):
        s[i+1] = s[i]+e[i]
    #print(s)
    ans = 0
    for i in range(N-K+1):
        ans = max(ans,s[i+K]-s[i])
    print(ans)
