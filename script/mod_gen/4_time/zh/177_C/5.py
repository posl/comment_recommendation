def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10**9 + 7
    ans = 0
    for i in range(n-1):
        for j in range(i+1, n):
            ans += a[i] * a[j]
            ans %= mod
    print(ans)

if __name__ == '__main__':
    main()