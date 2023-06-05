def gcd(x, y):
    if x < y:
        x, y = y, x
    while y > 0:
        x, y = y, x%y
    return x
n = int(input())
a = list(map(int, input().split()))
ans = 0
cnt = 0
for k in range(2, 1001):
    c = 0
    for i in range(n):
        if a[i] % k == 0:
            c += 1
    if cnt < c:
        cnt = c
        ans = k
print(ans)

if __name__ == '__main__':
    gcd()