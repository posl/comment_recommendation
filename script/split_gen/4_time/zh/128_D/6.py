def solve(n, k, v):
    ans = 0
    for i in range(0, min(n+1, k+1)):
        for j in range(0, min(n+1, k+1)):
            if i+j > k:
                continue
            l = i
            r = n - j
            a = v[:l] + v[r:]
            a.sort()
            ans = max(ans, sum(a[j:]))
    return ans
n, k = list(map(int, input().split()))
v = list(map(int, input().split()))
print(solve(n, k, v))
