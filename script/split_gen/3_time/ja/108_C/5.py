def main():
    N,K = map(int,input().split())
    ans = 0
    for a in range(1,N+1):
        b = a % K
        c = K - b
        if c == K:
            c = 0
        ans += (N//K)**3
        if b == 0:
            ans += (N//K + 1)**3
        if c == 0:
            ans += (N//K + 1)**3
        if b == c:
            ans -= (N//K + 1)**3
    print(ans)
