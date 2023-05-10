def gcd(a, b):
    if a < b:
        a, b = b, a
    while b > 0:
        a, b = b, a%b
    return a
n = int(input())
a = list(map(int, input().split()))
ans = 0
for k in range(2, max(a)+1):
    cnt = 0
    for i in range(n):
        if a[i] % k == 0:
            cnt += 1
    if cnt > ans:
        ans = cnt
print(ans)

if __name__ == '__main__':
    gcd()