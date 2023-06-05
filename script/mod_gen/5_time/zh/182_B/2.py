def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
n = int(input())
a = list(map(int, input().split()))
ans = 1
for i in range(2, 1001):
    cnt = 0
    for j in range(n):
        if a[j] % i == 0:
            cnt += 1
    if cnt >= ans:
        ans = i
print(ans)

if __name__ == '__main__':
    gcd()