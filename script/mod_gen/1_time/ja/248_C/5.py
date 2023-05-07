def main():
    n, m, k = map(int, input().split())
    ans = 0
    for i in range(1, m+1):
        ans += pow(m, n-1, 998244353) * i * (k-i*n+1) % 998244353
    print(ans%998244353)

if __name__ == '__main__':
    main()