def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
gcdness = 0
ans = 0
for i in range(2, a[0]+1):
    cnt = 0
    for j in range(n):
        if a[j] % i == 0:
            cnt += 1
    if cnt > gcdness:
        gcdness = cnt
        ans = i
print(ans)

if __name__ == '__main__':
    gcd()