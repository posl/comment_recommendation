Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b,c,d,e,f = map(int,input().split())
    x = a*b*c
    y = d*e*f
    print((x-y)%998244353)

=======
Suggestion 2

def main():
    A,B,C,D,E,F = map(int,input().split())
    print((A*B*C-D*E*F)%998244353)

=======
Suggestion 3

def main():
    #读取输入
    a,b,c,d,e,f = map(int,input().split())
    #计算结果
    ans = (a*b*c-d*e*f)%998244353
    #输出结果
    print(ans)

=======
Suggestion 4

def main():
    a,b,c,d,e,f = map(int,input().split())
    if a*b*c >= d*e*f:
        x = (a*b*c)%(998244353)
        y = (d*e*f)%(998244353)
        print(x-y)
    else:
        print("输入不符合要求")

=======
Suggestion 5

def main():
    a, b, c, d, e, f = map(int, input().split())
    print((a * b * c - d * e * f) % 998244353)

=======
Suggestion 6

def problems275_b():
    pass

=======
Suggestion 7

def problems275_b():
    A,B,C,D,E,F = map(int, input().split())
    print((A*B*C-D*E*F)%998244353)
