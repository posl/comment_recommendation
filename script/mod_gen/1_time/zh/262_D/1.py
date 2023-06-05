def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(1, n+1):
        ans += pow(2, n-i, 998244353) * pow(2, i-1, 998244353) * a[i-1]
        ans %= 998244353
    print(ans)

if __name__ == '__main__':
    main()