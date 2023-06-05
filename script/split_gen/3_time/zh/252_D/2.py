def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = [0] * (200000 + 1)
    for a in A:
        cnt[a] += 1
    ans = 0
    for i in range(1, 200000 + 1):
        if cnt[i] >= 3:
            ans += cnt[i] * (cnt[i] - 1) * (cnt[i] - 2) // 6
        if cnt[i] >= 2:
            ans += cnt[i] * (cnt[i] - 1) * (N - cnt[i])
        for j in range(i + 1, 200000 + 1):
            if cnt[i] >= 1 and cnt[j] >= 2:
                ans += cnt[i] * cnt[j] * (cnt[j] - 1) // 2
            if cnt[i] >= 2 and cnt[j] >= 1:
                ans += cnt[i] * (cnt[i] - 1) // 2 * cnt[j]
            if cnt[i] >= 1 and cnt[j] >= 1:
                k = i + j
                if k <= 200000 and cnt[k] >= 1:
                    ans += cnt[i] * cnt[j] * cnt[k]
    print(ans)
