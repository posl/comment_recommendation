Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B, C, D, E, F = map(int, input().split())
    print((A*B*C - D*E*F) % 998244353)

main()

=======
Suggestion 2

def main():
    A, B, C, D, E, F = map(int, input().split())
    print((A*B*C - D*E*F) % 998244353)

=======
Suggestion 3

def solve():
    A, B, C, D, E, F = map(int, input().split())
    print((A * B * C - D * E * F) % 998244353)

=======
Suggestion 4

def main():
    a, b, c, d, e, f = map(int, input().split())
    print((a*b*c-d*e*f)%998244353)

=======
Suggestion 5

def main():
    a, b, c, d, e, f = map(int, input().split())
    x = a * b * c
    y = d * e * f
    z = x - y
    print(z % 998244353)

=======
Suggestion 6

def modinv(a, m):
    """
    a^-1 (mod m)
    """
    b = m
    u = 1
    v = 0
    while b > 0:
        t = a // b
        a -= t * b
        a, b = b, a
        u -= t * v
        u, v = v, u
    u %= m
    if u < 0:
        u += m
    return u

=======
Suggestion 7

def main():
    # Read data
    A,B,C,D,E,F = map(int,input().split())

    # Calculate (A× B× C)-(D× E× F) mod 998244353
    print((A*B*C-D*E*F)%998244353)
