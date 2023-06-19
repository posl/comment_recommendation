def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
N = int(input())
A = list(map(int, input().split()))
left = [0] * (N + 1)
right = [0] * (N + 1)
for i in range(N):
    left[i + 1] = gcd(left[i], A[i])
    right[N - i - 1] = gcd(right[N - i], A[N - i - 1])
ans = 0
for i in range(N):
    ans = max(ans, gcd(left[i], right[i + 1]))
print(ans)
