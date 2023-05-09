def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
N, M = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
