Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, c, d, e, f = map(int, input().split())
    print((a*b*c - d*e*f) % 998244353)

=======
Suggestion 2

def main():
    A,B,C,D,E,F = map(int, input().split())
    print(((A*B*C)-(D*E*F))%998244353)

=======
Suggestion 3

def main():
    A,B,C,D,E,F = map(int, input().split())
    print((A*B*C-D*E*F)%998244353)

=======
Suggestion 4

def solve():
    A, B, C, D, E, F = map(int, input().split())
    print((A*B*C-D*E*F)%998244353)

=======
Suggestion 5

def main():
    A,B,C,D,E,F = map(int, input().split())
    ans = ((A*B*C) - (D*E*F)) % 998244353
    print(ans)

=======
Suggestion 6

def main():
    A,B,C,D,E,F = map(int,input().split())
    if A*B*C >= D*E*F:
        result = (A*B*C) - (D*E*F)
    else:
        result = (D*E*F) - (A*B*C)
    print(result%998244353)
main()
