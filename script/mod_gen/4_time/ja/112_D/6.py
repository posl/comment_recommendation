def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
n, m = map(int, input().split())
a = [int(i) for i in input().split()]
g = a[0]
for i in range(n):
    g = gcd(g, a[i])
print(g)

if __name__ == '__main__':
    gcd()