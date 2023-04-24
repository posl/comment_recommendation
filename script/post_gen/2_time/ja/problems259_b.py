Synthesizing 10/10 solutions

=======
Suggestion 1

def rotate(a,b,d):
    import math
    rad = math.radians(d)
    x = a * math.cos(rad) - b * math.sin(rad)
    y = a * math.sin(rad) + b * math.cos(rad)
    return x,y

a,b,d = map(int, input().split())
x,y = rotate(a,b,d)
print(x,y)

=======
Suggestion 2

def main():
    a, b, d = map(int, input().split())
    import math
    rad = math.radians(d)
    x = a*math.cos(rad) - b*math.sin(rad)
    y = a*math.sin(rad) + b*math.cos(rad)
    print(x, y)

=======
Suggestion 3

def main():
    a,b,d = map(int, input().split())
    import math
    rad = math.radians(d)
    x = a * math.cos(rad) - b * math.sin(rad)
    y = a * math.sin(rad) + b * math.cos(rad)
    print(x,y)

main()

=======
Suggestion 4

def solve():
    # -*- coding: utf-8 -*-
    # 整数の入力
    a,b,d = map(int, input().split())
    # スペース区切りの整数の入力
    #a = int(input())
    #b = int(input())
    # 出力
    #print("{} {}".format((a+b+c), s))
    #print("{}".format(s))
    #print("{:.10f} {:.10f}".format((a+b+c), s))
    #print("{:.10f}".format(s))
    #print("{:.10f} {:.10f}".format(a,b))
    #print("{:.10f} {:.10f}".format(a,b))
    print("{:.10f} {:.10f}".format(a,b))
    return 0

=======
Suggestion 5

def main():
    a,b,d = map(int,input().split())
    #print(a,b,d)
    x = a * math.cos(math.radians(d)) - b * math.sin(math.radians(d))
    y = a * math.sin(math.radians(d)) + b * math.cos(math.radians(d))
    print(x,y)
    return

=======
Suggestion 6

def main():
    import math
    a,b,d = map(int, input().split())
    rad = math.radians(d)
    cos = math.cos(rad)
    sin = math.sin(rad)
    x = a * cos - b * sin
    y = a * sin + b * cos
    print(x,y)

=======
Suggestion 7

def main():
    a,b,d = map(int,input().split())
    from math import cos,sin,pi
    rad = d * pi / 180
    x = a * cos(rad) - b * sin(rad)
    y = a * sin(rad) + b * cos(rad)
    print(x,y)

=======
Suggestion 8

def rotate(x,y,d):
    import math
    rad = math.radians(d)
    x_dash = x*math.cos(rad) - y*math.sin(rad)
    y_dash = x*math.sin(rad) + y*math.cos(rad)
    return [x_dash,y_dash]

a,b,d = input().split()
a = float(a)
b = float(b)
d = float(d)
x,y = rotate(a,b,d)
print(x,y)

=======
Suggestion 9

def rotate(x, y, d):
    from math import cos, sin, radians
    a = cos(radians(d))
    b = sin(radians(d))
    return a*x - b*y, b*x + a*y

a, b, d = map(int, input().split())
x, y = rotate(a, b, d)
print(x, y)

=======
Suggestion 10

def main():
    a, b, d = map(int, input().split())
    #print(a, b, d)
    #print(math.cos(math.radians(d)))
    #print(math.sin(math.radians(d)))
    print(a * math.cos(math.radians(d)) - b * math.sin(math.radians(d)), a * math.sin(math.radians(d)) + b * math.cos(math.radians(d)))
