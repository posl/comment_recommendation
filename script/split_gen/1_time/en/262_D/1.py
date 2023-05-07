def main():
    N = int(input())
    A = list(map(int,input().split()))
    mod = 998244353
    ans = 0
    for i in range(N):
        ans += pow(2,i,mod)*pow(2,N-i-1,mod)*A[i]
        ans %= mod
    print(ans)
