def main():
    n,k = map(int, input().split())
    #n,k = 200000,200001
    #n,k = 141421,35623
    mod = 10**9+7
    ans = 0
    for i in range(k,n+2):
        min = (i-1)*i//2
        max = (2*n-i+1)*i//2
        ans += max-min+1
        ans %= mod
    print(ans)
