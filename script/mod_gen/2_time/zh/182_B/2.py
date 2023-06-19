def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)
n = int(input())
a = list(map(int, input().split()))
a.sort()
a.reverse()
ans = 0
cnt = 0
for i in range(2, a[0]+1):
    c = 0
    for j in range(n):
        if a[j] % i == 0:
            c += 1
    if cnt < c:
        cnt = c
        ans = i
print(ans)

if __name__ == '__main__':
    gcd()