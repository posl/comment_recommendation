def main():
    N, K = map(int, input().split())
    mod = 10**9+7
    ans = 0
    for i in range(K, N+2):
        ans += (N+1)*i - i*(i-1) + 1
        ans %= mod
    print(ans)
main()

if __name__ == '__main__':
    main()