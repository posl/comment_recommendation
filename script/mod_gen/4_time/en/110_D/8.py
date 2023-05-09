def main():
    import sys
    input = sys.stdin.readline
    N, M = map(int, input().split())
    ans = 1
    MOD = 10**9 + 7
    for i in range(2, int(M**0.5) + 1):
        if M % i == 0:
            cnt = 0
            while M % i == 0:
                M //= i
                cnt += 1
            ans *= comb(cnt + N - 1, N - 1, MOD)
            ans %= MOD
    if M > 1:
        ans *= N
        ans %= MOD
    print(ans)

if __name__ == '__main__':
    main()