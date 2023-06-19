def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a%b)
n = int(input())
a = list(map(int, input().split()))
ans = 0
max_gcdness = 0
for i in range(2, 1001):
    gcdness = 0
    for j in range(n):
        if a[j] % i == 0:
            gcdness += 1
    if max_gcdness < gcdness:
        max_gcdness = gcdness
        ans = i
print(ans)

if __name__ == '__main__':
    gcd()