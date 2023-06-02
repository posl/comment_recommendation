Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B, C, D, E, F = map(int, input().split())
    print((A*B*C-D*E*F)%998244353)

=======
Suggestion 2

def main():
    a,b,c,d,e,f = map(int,input().split())
    print(((a*b*c)-(d*e*f))%998244353)

=======
Suggestion 3

def main():
    a, b, c, d, e, f = map(int, input().split())
    ans = (a * b * c - d * e * f) % 998244353
    print(ans)

=======
Suggestion 4

def main():
    A,B,C,D,E,F=map(int,input().split())
    if A*B*C>=D*E*F:
        print((A*B*C-D*E*F)%998244353)
    else:
        print((D*E*F-A*B*C)%998244353)
main()

=======
Suggestion 5

def main():
    A, B, C, D, E, F = map(int, input().split())
    print(((A * B * C) - (D * E * F)) % 998244353)

=======
Suggestion 6

def problems275_b():
    #输入
    A, B, C, D, E, F = map(int, input().split())

    #计算
    ans = (A*B*C) % 998244353 - (D*E*F) % 998244353

    #输出
    print(ans % 998244353)

=======
Suggestion 7

def main():
    a,b,c,d,e,f=map(int,input().split())
    print((a*b*c-d*e*f)%998244353)

=======
Suggestion 8

def cal(a,b,c,d,e,f):
    if a*b*c >= d*e*f:
        return (a*b*c)%(998244353)-(d*e*f)%(998244353)
    else:
        return (d*e*f)%(998244353)-(a*b*c)%(998244353)

=======
Suggestion 9

def main():
    a,b,c,d,e,f = map(int,input().split())
    A = a*b*c
    B = d*e*f
    if A > B:
        print((A-B)%998244353)
    else:
        print((B-A)%998244353)
