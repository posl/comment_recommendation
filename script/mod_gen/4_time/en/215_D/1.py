def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
a = list(set(a))
x = [1] * (m + 1)
for i in a:
    for j in range(i, m + 1, i):
        x[j] = 0
y = [i for i in range(1, m + 1) if x[i] == 1]
print(len(y))
for i in y:
    print(i)

if __name__ == '__main__':
    gcd()