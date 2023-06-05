def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
a, b, k = map(int, input().split())
c = gcd(a, b)
l = []
for i in range(1, c + 1):
    if c % i == 0:
        l.append(i)
print(l[-k])

if __name__ == '__main__':
    gcd()