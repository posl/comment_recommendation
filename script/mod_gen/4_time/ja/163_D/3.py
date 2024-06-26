def main():
    n, k = map(int, input().split())
    ans = 0
    mod = 10**9+7
    for i in range(k, n+2):
        ans += i*n-i*(i-1)+1
        ans %= mod
    print(ans)

if __name__ == '__main__':
    main()