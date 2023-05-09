def main():
    N, M = map(int, input().split())
    mod = 1000000007
    ans = 1
    for i in range(2, int(M ** 0.5) + 1):
        if M % i == 0:
            cnt = 0
            while M % i == 0:
                M //= i
                cnt += 1
            ans = ans * (pow(i, cnt * N, mod) - pow(i, (cnt - 1) * N, mod)) % mod
    if M > 1:
        ans = ans * (pow(M, N, mod) - pow(M, N - 1, mod)) % mod
    print(ans)

if __name__ == '__main__':
    main()