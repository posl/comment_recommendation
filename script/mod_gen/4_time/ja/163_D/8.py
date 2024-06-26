def main():
    N, K = map(int, input().split())
    mod = 10**9 + 7
    res = 0
    for i in range(K, N+2):
        res += (i * (2 * N - i + 1)) // 2 - (i * (i - 1)) // 2 + 1
        res = res % mod
    print(res)

if __name__ == '__main__':
    main()