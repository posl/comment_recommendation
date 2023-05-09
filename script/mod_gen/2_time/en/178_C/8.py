def main():
    N = int(input())
    MOD = 10**9 + 7
    ans = 0
    for i in range(1, N+1):
        ans += 2 * (10**i - 9**i) + 8**i
    print(ans % MOD)

if __name__ == '__main__':
    main()