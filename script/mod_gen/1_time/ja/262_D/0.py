def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    ans = 0
    for i in range(1, N+1):
        ans += pow(2, i-1, MOD) * pow(2, N-i, MOD) * i * A[i-1]
        ans %= MOD
    print(ans)

if __name__ == '__main__':
    main()