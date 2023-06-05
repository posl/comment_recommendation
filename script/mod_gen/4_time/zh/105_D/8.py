def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    cnt = [0] * m
    for i in range(n + 1):
        cnt[s[i] % m] += 1
    ans = 0
    for i in range(m):
        ans += cnt[i] * (cnt[i] - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()