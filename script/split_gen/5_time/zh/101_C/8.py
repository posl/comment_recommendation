def solve(n, k, a):
    ans = 0
    for i in range(n-k):
        ans += 1
    if (n-k) % (k-1) != 0:
        ans += 1
    return ans
n, k = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, k, a))
