def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    s = sum(p[:k])
    ans = s
    for i in range(n-k):
        s = s - p[i] + p[i+k]
        ans = max(ans,s)
    print((ans+k)/2)
