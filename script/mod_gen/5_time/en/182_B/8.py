def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
n = int(input())
a = list(map(int, input().split()))
a.sort()
a.reverse()
ans = 0
cnt = 0
for i in range(2, a[0]+1):
    tmp = 0
    for j in range(n):
        if a[j]%i == 0:
            tmp += 1
    if tmp >= cnt:
        ans = i
        cnt = tmp
print(ans)

if __name__ == '__main__':
    gcd()