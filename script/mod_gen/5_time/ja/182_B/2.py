def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)
n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(2, 1001):
    cnt = 0
    for j in range(n):
        if a[j] % i == 0:
            cnt += 1
    if cnt > ans:
        ans = cnt
print(ans)

if __name__ == '__main__':
    gcd()