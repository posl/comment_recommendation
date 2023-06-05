def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    cnt = {}
    for x in s:
        if x % m in cnt:
            cnt[x % m] += 1
        else:
            cnt[x % m] = 1
    ans = 0
    for v in cnt.values():
        ans += v * (v - 1) // 2
    print(ans)
