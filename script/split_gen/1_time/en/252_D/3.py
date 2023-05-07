def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [0] * (10**5 + 1)
    for i in range(n):
        cnt[a[i]] += 1
    ans = 0
    for i in range(1, 10**5+1):
        ans += cnt[i] * (cnt[i] - 1) * (cnt[i] - 2) // 6
    for i in range(1, 10**5-1):
        for j in range(i+1, 10**5):
            ans += cnt[i] * cnt[j] * (cnt[j] - 1) // 2
    for i in range(1, 10**5):
        for j in range(i+1, 10**5+1):
            ans += cnt[i] * (cnt[i] - 1) // 2 * cnt[j]
    print(ans)
