def solve(n, a):
    from collections import defaultdict
    d = defaultdict(int)
    for i in range(n):
        d[a[i]] += 1
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] * a[j] in d:
                ans += d[a[i]*a[j]]
    return ans
n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))
