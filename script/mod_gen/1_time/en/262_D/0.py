def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    ans = 0
    for i in range(N):
        ans += pow(2, i, MOD) * (pow(2, N - i - 1, MOD) - 1) * A[i]
        ans %= MOD
    print(ans)

if __name__ == '__main__':
    main()