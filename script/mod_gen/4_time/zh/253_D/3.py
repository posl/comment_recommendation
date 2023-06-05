def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
N, a, b = map(int, input().split())
g = gcd(a, b)
lcm = a * b // g
print((N // a + N // b - N // lcm) * (N + 1) - N)

if __name__ == '__main__':
    gcd()