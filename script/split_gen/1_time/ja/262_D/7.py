def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    #print(N, A)
    #print(MOD)
    sum = 0
    for i in range(N):
        sum += A[i]
    #print(sum)
    sum = sum * pow(2, MOD - 2, MOD)
    sum = sum % MOD
    #print(sum)
    ans = sum * pow(2, N - 1, MOD)
    ans = ans % MOD
    print(ans)
