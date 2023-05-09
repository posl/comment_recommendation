def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10**9+7
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(n):
            if a[j] & (1 << i):
                cnt += 1
        ans += (1 << i) * cnt * (n - cnt)
        ans %= mod
    print(ans)
main()

if __name__ == '__main__':
    main()