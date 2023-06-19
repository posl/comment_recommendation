def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a%b
    return a
n = int(input())
a = list(map(int, input().split()))
ans = 0
max = 0
for k in range(2, 1001):
    cnt = 0
    for i in a:
        if i%k == 0:
            cnt += 1
    if cnt > max:
        ans = k
        max = cnt
print(ans)
