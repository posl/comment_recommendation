def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
n = int(input())
a = list(map(int, input().split()))
ans = 0
cnt = 0
for i in range(2, 1001):
    c = 0
    for j in a:
        if j % i == 0:
            c += 1
    if c > cnt:
        ans = i
        cnt = c
print(ans)
