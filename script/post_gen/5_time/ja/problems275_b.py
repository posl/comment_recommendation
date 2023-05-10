Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A,B,C,D,E,F = map(int,input().split())
    print((A*B*C-D*E*F)%998244353)

=======
Suggestion 2

def main():
    a, b, c, d, e, f = map(int, input().split())
    mod = 998244353
    print(((a * b * c) - (d * e * f)) % mod)

=======
Suggestion 3

def main():
    A, B, C, D, E, F = map(int, input().split())
    MOD = 998244353
    print(((A * B * C) - (D * E * F)) % MOD)

=======
Suggestion 4

def main():
    a,b,c,d,e,f = map(int, input().split())
    print(((a*b*c)-(d*e*f))%998244353)

main()

=======
Suggestion 5

def main():
    a,b,c,d,e,f = map(int, input().split())
    if a*b*c >= d*e*f:
        print((a*b*c - d*e*f) % 998244353)
    else:
        print((d*e*f - a*b*c) % 998244353)

=======
Suggestion 6

def main():
    a,b,c,d,e,f = map(int,input().split())
    print((a*b*c-d*e*f)%998244353)

=======
Suggestion 7

def main():
    a,b,c,d,e,f = map(int, input().split())
    ans = (a*b*c - d*e*f) % 998244353
    print(ans)
