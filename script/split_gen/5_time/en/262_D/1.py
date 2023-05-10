def main():
    N = int(input())
    A = list(map(int,input().split()))
    mod = 998244353
    ans = 0
    for i in range(N):
        ans = (ans + A[i])%mod
    ans = ans * pow(2,N-1,mod)
    ans = ans % mod
    print(ans)
