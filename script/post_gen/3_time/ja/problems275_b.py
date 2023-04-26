Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B, C, D, E, F = map(int, input().split())
    print((A*B*C-D*E*F) % 998244353)

=======
Suggestion 2

def main():
    A, B, C, D, E, F = map(int, input().split())
    mod = 998244353
    ans = (A*B*C - D*E*F) % mod
    print(ans)

=======
Suggestion 3

def main():
    a, b, c, d, e, f = map(int, input().split())
    print((a*b*c-d*e*f) % 998244353)

=======
Suggestion 4

def modinv(x):
    return pow(x, 998244353-2, 998244353)

=======
Suggestion 5

def main():
    # A,B,C,D,E,F = map(int,input().split())
    A, B, C,

=======
Suggestion 6

def divmod(a, b):
    return a // b, a % b
