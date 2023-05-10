def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [0] * (10 ** 5 + 1)
    for i in range(n):
        cnt[a[i]] += 1
    ans = 0
    for i in range(1, 10 ** 5 + 1):
        ans += cnt[i] * (cnt[i] - 1) * (cnt[i] - 2) // 6
    for i in range(1, 10 ** 5 + 1):
        ans += cnt[i] * (cnt[i] - 1) // 2 * (n - cnt[i])
    for i in range(1, 10 ** 5 + 1):
        ans += cnt[i] * (cnt[i] - 1) // 2 * (cnt[i] - 2) // 3
    print(ans)

if __name__ == '__main__':
    main()