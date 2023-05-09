def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
N = int(input())
A = list(map(int, input().split()))
left = [0] * N
right = [0] * N
left[0] = A[0]
right[N - 1] = A[N - 1]
for i in range(1, N):
    left[i] = gcd(left[i - 1], A[i])
for i in range(N - 2, -1, -1):
    right[i] = gcd(right[i + 1], A[i])
ans = 0
for i in range(N):
    if i == 0:
        ans = max(ans, right[1])
    elif i == N - 1:
        ans = max(ans, left[N - 2])
    else:
        ans = max(ans, gcd(left[i - 1], right[i + 1]))
print(ans)
