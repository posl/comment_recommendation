def solve(n, a):
    from collections import Counter
    cnt = Counter(a)
    ans = 0
    for k, v in cnt.items():
        if v >= 3:
            ans += v * (v - 1) * (v - 2) // 6
        elif v == 2:
            ans += cnt[k + 1] + cnt[k - 1]
        else:
            ans += cnt[k + 1] + cnt[k + 2]
    return ans
n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))

if __name__ == '__main__':
    solve()