def main():
    N, K = map(int, input().split())
    mod = 10**9+7
    ans = 0
    for i in range(K, N+2):
        ans += (i*(N+1-i)+1)%mod
        ans %= mod
    print(ans)

if __name__ == '__main__':
    main()