Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

=======
Suggestion 2

def gcd(x, y):
    if x < y:
        x, y = y, x
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

a, b = map(int, input().split())
print(a * b // gcd(a, b))

=======
Suggestion 3

def lcm(x, y):
    import math
    return (x * y) // math.gcd(x, y)

=======
Suggestion 4

def main():
    # 读取输入
    A, B = map(int, input().split())

    # 输出
    print(A * B)

=======
Suggestion 5

def gcd(a,b):
    if a<b:
        a,b=b,a
    while b!=0:
        a,b=b,a%b
    return a

a,b=map(int,input().split())
g=gcd(a,b)
print(a*b//g)

=======
Suggestion 6

def lcm(a, b):
    from fractions import gcd
    return a * b / gcd(a, b)

a,b = map(int,input().split())
print(int(lcm(a,b)))

=======
Suggestion 7

def lcm(a,b):
    from fractions import gcd
    return a*b//gcd(a,b)

a,b = map(int,input().split())
print(lcm(a,b))

=======
Suggestion 8

def gcd(a, b):
    if a < b:
        a, b = b, a
    while a % b != 0:
        a, b = b, a % b
    return b

a, b = map(int, input().split())
g = gcd(a, b)
print(a * b // g)

=======
Suggestion 9

def main():
    a,b = map(int, input().split())
    print((a*b)//math.gcd(a,b))
