def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
N = int(input())
A = list(map(int, input().split()))
left = [0] * (N + 1)
for i in range(N):
    left[i + 1] = gcd(left[i], A[i])
right = [0] * (N + 1)
for i in range(N - 1, -1, -1):
    right[i] = gcd(right[i + 1], A[i])
ans = 1
for i in range(N):
    ans = max(ans, gcd(left[i], right[i + 1]))
print(ans)

if __name__ == '__main__':
    gcd()