def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
A, B, C, D = map(int, input().split())
g = gcd(C, D)
lcm = C * D // g

if __name__ == '__main__':
    gcd()