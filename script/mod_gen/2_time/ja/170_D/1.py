def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
N = int(input())
A = list(map(int, input().split()))
L = [0] * (N + 1)
R = [0] * (N + 1)
for i in range(1, N + 1):
    L[i] = gcd(L[i - 1], A[i - 1])
    R[N - i] = gcd(R[N - i + 1], A[N - i])
ans = 0
for i in range(N):
    ans = max(ans, gcd(L[i], R[i + 1]))
print(ans)

if __name__ == '__main__':
    gcd()