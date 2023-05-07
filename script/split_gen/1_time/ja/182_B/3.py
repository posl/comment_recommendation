def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
N = int(input())
A = list(map(int, input().split()))
ans = 0
for i in range(2, 1001):
    cnt = 0
    for j in range(N):
        if A[j] % i == 0:
            cnt += 1
    if ans < cnt:
        ans = cnt
print(ans)
