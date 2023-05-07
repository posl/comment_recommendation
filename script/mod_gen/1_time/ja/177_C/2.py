def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10**9+7
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            ans += (A[i] * A[j]) % MOD
            ans %= MOD
    print(ans)

if __name__ == '__main__':
    main()