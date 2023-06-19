def gcd(a,b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
n = int(input())
a = list(map(int,input().split()))
a.sort(reverse=True)
ans = 0
cnt = 0
for i in range(2,1001):
    tmp = 0
    for j in range(n):
        if a[j] % i == 0:
            tmp += 1
    if tmp > cnt:
        cnt = tmp
        ans = i
print(ans)

if __name__ == '__main__':
    gcd()