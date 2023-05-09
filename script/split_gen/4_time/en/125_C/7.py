def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)
N = int(input())
A = list(map(int, input().split()))
left = [0] * (N + 1)
right = [0] * (N + 1)
for i in range(1, N + 1):
    left[i] = gcd(left[i - 1], A[i - 1])
for i in range(N - 1, -1, -1):
    right[i] = gcd(right[i + 1], A[i])
ans = 0
for i in range(N):
    ans = max(ans, gcd(left[i], right[i + 1]))
print(ans)
