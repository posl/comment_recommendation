def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    ans = 0
    for i in range(n):
        s -= a[i]
        ans += a[i] * s
        ans %= 10**9+7
    print(ans)

if __name__ == '__main__':
    main()