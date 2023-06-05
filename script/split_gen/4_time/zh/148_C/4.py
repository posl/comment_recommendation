def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
A, B = map(int,input().split())
C = gcd(A, B)
D = A * B / C
print(int(D))
