def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
N = int(input())
A = list(map(int, input().split()))
ans = 0
for i in range(2, max(A) + 1):
    cnt = 0
    for j in A:
        if j % i == 0:
            cnt += 1
    if cnt >= ans:
        ans = cnt
        num = i
print(num)
