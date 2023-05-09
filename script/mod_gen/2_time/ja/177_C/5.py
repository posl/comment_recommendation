def main():
    n = int(input())
    a = list(map(int, input().split()))
    MOD = 10**9 + 7
    ans = 0
    s = 0
    for i in range(n):
        s += a[i]
    for i in range(n):
        s -= a[i]
        ans += a[i] * s
        ans %= MOD
    print(ans)

if __name__ == '__main__':
    main()