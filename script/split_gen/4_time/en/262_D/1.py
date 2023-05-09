def main():
    N = int(input())
    A = [int(a) for a in input().split()]
    mod = 998244353
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            if (A[i]+A[j])%2 == 0:
                ans += 2**(N-2)
                ans %= mod
    print(ans)
