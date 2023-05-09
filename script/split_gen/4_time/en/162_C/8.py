def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
k = int(input())
total = 0
for i in range(1, k+1):
    for j in range(1, k+1):
        temp = gcd(i, j)
        for l in range(1, k+1):
            total += gcd(temp, l)
print(total)
