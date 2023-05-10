def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
n = int(input())
a = list(map(int, input().split()))
# a = [int(i) for i in input().split()]
a.sort()
g = a[0]
for i in range(1, n):
    g = gcd(g, a[i])
print(g)

if __name__ == '__main__':
    gcd()