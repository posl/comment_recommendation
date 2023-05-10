def main():
    n, k = map(int, input().split())
    mod = 10**9+7
    ans = 0
    for i in range(k, n+2):
        ans += (n+1-i)*i+1
    print(ans%mod)

if __name__ == '__main__':
    main()