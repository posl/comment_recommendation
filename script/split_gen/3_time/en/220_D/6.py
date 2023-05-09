def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    MOD = 998244353
    ans = [0]*10
    for i in range(10):
        if i == A[0]:
            ans[i] = pow(2,N-1,MOD)
    for i in range(1,N):
        for j in range(10):
            ans[j] = (ans[j]*pow(2,MOD-2,MOD)+ans[(j-A[i])%10])%MOD
    print(*ans, sep='
')
