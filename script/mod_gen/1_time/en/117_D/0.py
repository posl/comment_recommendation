def solve(n, k, a):
    b = [0] * (n + 1)
    for i in range(n):
        b[i + 1] = b[i] ^ a[i]
    ans = 0
    for i in range(n + 1):
        for j in range(i + 1, n + 1):
            if b[i] ^ b[j] <= k:
                ans = max(ans, b[i] + b[j])
    return ans
n, k = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, k, a))
