def solve(n, a):
    ans = [0] * n
    from collections import defaultdict
    d = defaultdict(int)
    for i in range(n):
        ans[i] = i - d[a[i]]
        d[a[i]] += 1
    return ans
n = int(input())
a = list(map(int, input().split()))
print(*solve(n, a), sep='\n')
