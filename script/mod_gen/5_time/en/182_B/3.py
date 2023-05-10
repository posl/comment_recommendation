def gcd(a, b):
    if a < b:
        a, b = b, a
    while b > 0:
        r = a % b
        a, b = b, r
    return a
N = int(input())
A = list(map(int, input().split()))
A.sort()
ans = 0
cnt = 0
for k in range(2, A[-1]+1):
    c = 0
    for i in range(N):
        if A[i] % k == 0:
            c += 1
    if c > cnt:
        ans = k
        cnt = c
print(ans)

if __name__ == '__main__':
    gcd()