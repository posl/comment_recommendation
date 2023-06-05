Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def problem275_b():
    A,B,C,D,E,F = map(int, input().split())
    print((A*B*C-D*E*F)%998244353)

=======
Suggestion 2

def problems275_b():
    A, B, C, D, E, F = map(int, input().split())
    print((A * B * C - D * E * F) % 998244353)

=======
Suggestion 3

def problems275_b(A,B,C,D,E,F):
    if A*B*C>=D*E*F:
        return (A*B*C-D*E*F)%998244353
    else:
        return (D*E*F-A*B*C)%998244353

=======
Suggestion 4

def main():
    A, B, C, D, E, F = map(int, input().split())
    print((A*B*C - D*E*F) % 998244353)

=======
Suggestion 5

def main():
    A, B, C, D, E, F = [int(i) for i in input().split()]
    print((A * B * C - D * E * F) % 998244353)

=======
Suggestion 6

def main():
    a,b,c,d,e,f = map(int, input().split())
    if a*b*c >= d*e*f:
        print((a*b*c - d*e*f)%998244353)
    else:
        print(0)

=======
Suggestion 7

def problems275_b(a,b,c,d,e,f):
    if a*b*c >= d*e*f:
        return (a*b*c - d*e*f) % 998244353
    else:
        return 0

=======
Suggestion 8

def solve():
    a, b, c, d, e, f = map(int, input().split())
    ans = (a*b*c-d*e*f)%998244353
    print(ans)

=======
Suggestion 9

def main():
    # 读取输入
    a,b,c,d,e,f = map(int, input().split())
    # 计算结果
    result = a*b*c - d*e*f
    # 打印结果
    print(result%998244353)
