def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
N = int(input())
A = list(map(int, input().split()))
left = [0] * (N + 1)
right = [0] * (N + 1)
for i in range(N):
    left[i + 1] = gcd(left[i], A[i])
    right[N - i - 1] = gcd(right[N - i], A[N - i - 1])
ans = 1
for i in range(N):
    ans = max(ans, gcd(left[i], right[i + 1]))
print(ans)
