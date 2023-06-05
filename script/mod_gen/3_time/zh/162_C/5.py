def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
k = int(input())
sum = 0
for a in range(1, k+1):
    for b in range(1, k+1):
        for c in range(1, k+1):
            sum += gcd(a, gcd(b, c))
print(sum)

if __name__ == '__main__':
    gcd()