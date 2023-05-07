def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
n = int(input())
a = list(map(int, input().split()))
a.sort()
b = [a[0]]
for i in range(1, n):
    b.append(gcd(a[i], b[i - 1]))
b.sort()
c = [0] * 1001
for i in range(n):
    for j in range(2, a[i] + 1):
        if a[i] % j == 0:
            c[j] += 1
print(c.index(max(c)))

if __name__ == '__main__':
    gcd()