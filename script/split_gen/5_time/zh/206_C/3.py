def solve(n, a):
    cnt = [0] * (10 ** 9 + 1)
    for i in range(n):
        cnt[a[i]] += 1
    ans = 0
    for i in range(1, 10 ** 9 + 1):
        ans += cnt[i] * (cnt[i] - 1) // 2
    return ans
n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))
