def main():
    N = int(input())
    MOD = 10**9 + 7
    ans = 0
    for i in range(N+1):
        ans += pow(10, i, MOD) * pow(9, N-i, MOD) * pow(8, i, MOD)
        ans %= MOD
    print(ans)

if __name__ == '__main__':
    main()