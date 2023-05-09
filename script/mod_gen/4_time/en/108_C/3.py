def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
N, K = map(int, input().split())
ans = 0
for i in range(1, N+1):
    if i % K == 0:
        ans += N // K
    elif i % K * 2 == K:
        ans += N // K + 1
    else:
        ans += N // K + 1 - (N % K - i % K) // gcd(K, N % K)
print(ans)

if __name__ == '__main__':
    gcd()