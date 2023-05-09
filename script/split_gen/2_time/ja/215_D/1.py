def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
N, M = map(int, input().split())
A = list(map(int, input().split()))
