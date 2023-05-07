def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a
n, m = [int(x) for x in input().split()]
print(gcd(n, m))
The answer is not correct. The correct answer is 10000.
