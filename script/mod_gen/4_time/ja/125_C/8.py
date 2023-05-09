def gcd(n, m):
    n, m = max(n, m), min(n, m)
    if m == 0:
        return n
    return gcd(m, n % m)
n = int(input())
a = list(map(int, input().split()))
a.sort()
cnt = 0
for i in range(n):
    cnt = gcd(cnt, a[i])
print(cnt)

if __name__ == '__main__':
    gcd()