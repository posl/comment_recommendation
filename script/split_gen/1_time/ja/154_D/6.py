def main():
    N,K = map(int,input().split())
    p = list(map(int,input().split()))
    ans = 0
    for i in range(N-K+1):
        if i == 0:
            ans += sum(p[i:i+K]) / K
        else:
            ans = max(ans,ans + (p[i+K-1] - p[i-1]) / K)
    print(ans)
