def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
n = int(input())
a = list(map(int, input().split()))
cnt = [0] * (max(a) + 1)
for i in a:
    cnt[i] += 1
ans = 0
for i in range(1, max(a) + 1):
    for j in range(i, max(a) + 1, i):
        if cnt[j] == 0:
            continue
        if i == j:
            ans += cnt[i] * (cnt[i] - 1) * (cnt[i] - 2) // 6
        elif i < j:
            k = gcd(i, j)
            if k == i:
                ans += cnt[i] * cnt[j] * (cnt[j] - 1) // 2
            elif k == j:
                ans += cnt[i] * cnt[j] * (cnt[i] - 1) // 2
            else:
                ans += cnt[i] * cnt[j] * cnt[k]
print(ans)
