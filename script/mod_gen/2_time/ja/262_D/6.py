def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
N = int(input())
A = list(map(int, input().split()))
A.sort()
A.reverse()
ans = 0
for i in range(1, N):
    for j in range(i + 1, N + 1):
        ans += gcd(A[i - 1], A[j - 1]) * (2 ** (N - j))
        ans %= 998244353
for i in range(1, N + 1):
    ans += A[i - 1] * (2 ** (N - i))
    ans %= 998244353
print(ans)

if __name__ == '__main__':
    gcd()