Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def func():
    A, B, C, D, E, F = map(int, input().split())
    if A * B * C >= D * E * F:
        print((A * B * C) % 998244353 - (D * E * F) % 998244353)
    else:
        print((D * E * F) % 998244353 - (A * B * C) % 998244353)

=======
Suggestion 2

def main():
    A,B,C,D,E,F = map(int,input().split())
    print((A*B*C-D*E*F)%998244353)

=======
Suggestion 3

def problems275_b():
    a,b,c,d,e,f = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    e = int(e)
    f = int(f)
    if a*b*c >= d*e*f:
        print((a*b*c - d*e*f)%998244353)
    else:
        print(0)

=======
Suggestion 4

def problem275_b():
    a,b,c,d,e,f = map(int,input().split())
    #print(a,b,c,d,e,f)
    if a*b*c >= d*e*f:
        print((a*b*c - d*e*f)%998244353)
    else:
        print((d*e*f - a*b*c)%998244353)

=======
Suggestion 5

def main():
    # 读取输入
    A, B, C, D, E, F = map(int, input().split())

    # 计算答案
    ans = (A * B * C - D * E * F) % 998244353

    # 输出结果
    print(ans)

=======
Suggestion 6

def main():
    a,b,c,d,e,f = map(int, input().split())
    print((a*b*c-d*e*f)%998244353)

=======
Suggestion 7

def f(A, B, C, D, E, F):
    return (A*B*C-D*E*F)%998244353

=======
Suggestion 8

def main():
    a,b,c,d,e,f = map(int,input().split())
    x = a*b*c - d*e*f
    print(x%998244353)
