def main():
    N = int(input())
    ans = 0
    for i in range(1, 18):
        ans += (N // 10**i) * 9 * 10**(i - 1)
        ans += max(0, N % 10**i - 10**(i - 1) + 1)
    ans %= 998244353
    print(ans)

if __name__ == '__main__':
    main()