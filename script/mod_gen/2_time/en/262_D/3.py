def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 998244353
    ans = 0
    for i in range(1, n+1):
        ans += pow(2, i-1, mod) * pow(2, n-i, mod) * a[i-1]
    print(ans%mod)

if __name__ == '__main__':
    main()