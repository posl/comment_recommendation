def solve(n, k, h):
    h.sort(reverse=True)
    ans = sum(h)
    for i in range(k):
        ans -= h[i]
    return ans
n, k = map(int, input().split())
h = list(map(int, input().split()))
print(solve(n, k, h))
