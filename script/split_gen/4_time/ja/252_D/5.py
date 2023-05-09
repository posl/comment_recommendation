def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    cnt = [0] * (10 ** 6 + 1)
    for j in range(n):
        cnt[a[j]] += 1
    for i in range(1, 10 ** 6 + 1):
        ans += cnt[i] * (cnt[i] - 1) * (cnt[i] - 2) // 6
    for i in range(1, 10 ** 6 + 1):
        ans += cnt[i] * (cnt[i] - 1) // 2 * (n - cnt[i])
    for i in range(1, 10 ** 6 + 1):
        ans += cnt[i] * (cnt[i] - 1) // 2 * (cnt[i] - 2) // 3
    print(ans)
