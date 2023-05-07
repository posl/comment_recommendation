def main():
    N = int(input())
    ans = 0
    for i in range(1, 19):
        ans += (N // 10**i) * 10**(i-1)
        ans += max(min(N % 10**i - 10**(i-1) + 1, 10**(i-1)), 0)
    print(ans % 998244353)

if __name__ == '__main__':
    main()