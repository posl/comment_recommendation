def main():
    N = int(input())
    mod = 998244353
    ans = 0
    for i in range(1, len(str(N)) + 1):
        ans += (N - 10 ** (i - 1) + 1) * i
        ans %= mod
    print(ans)

if __name__ == '__main__':
    main()