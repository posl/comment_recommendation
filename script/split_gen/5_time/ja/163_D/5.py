def main():
    n,k = map(int,input().split())
    mod = 10**9+7
    ans = 0
    for i in range(k,n+2):
        ans += (n+1-i)*i+1
        ans %= mod
    print(ans)
