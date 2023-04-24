Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b, d = map(int, input().split())
    print(a * math.cos(math.radians(d)) - b * math.sin(math.radians(d)), a * math.sin(math.radians(d)) + b * math.cos(math.radians(d)))

=======
Suggestion 2

def main():
    import math
    a,b,d = map(int,input().split())
    d = math.radians(d)
    print(a*math.cos(d)-b*math.sin(d),a*math.sin(d)+b*math.cos(d))

=======
Suggestion 3

def main():
    from math import cos, sin, radians
    a, b, d = map(int, input().split())
    d = radians(d)
    print(a*cos(d)-b*sin(d), a*sin(d)+b*cos(d))

=======
Suggestion 4

def rotate(x, y, r):
    import math
    x1 = x * math.cos(math.radians(r)) - y * math.sin(math.radians(r))
    y1 = x * math.sin(math.radians(r)) + y * math.cos(math.radians(r))
    return x1, y1

a, b, d = map(int, input().split())
x1, y1 = rotate(a, b, d)
print(x1, y1)

=======
Suggestion 5

def main():
    a, b, d = map(int,input().split())
    rad = d * math.pi / 180
    print(a * math.cos(rad) - b * math.sin(rad), a * math.sin(rad) + b * math.cos(rad))

=======
Suggestion 6

def rotation(x,y,d):
    import math
    r = math.radians(d)
    x2 = x * math.cos(r) - y * math.sin(r)
    y2 = x * math.sin(r) + y * math.cos(r)
    return x2, y2

a, b, d = map(int, input().split())
x2, y2 = rotation(a,b,d)
print(x2, y2)

=======
Suggestion 7

def main():
    import math
    a,b,d = map(int,input().split())
    rad = math.radians(d)
    print(a*math.cos(rad) - b*math.sin(rad),a*math.sin(rad) + b*math.cos(rad))

=======
Suggestion 8

def main():
    #入力
    a,b,d = map(int, input().split())
    #処理
    import math
    d = math.radians(d)
    x = a * math.cos(d) - b * math.sin(d)
    y = a * math.sin(d) + b * math.cos(d)
    #出力
    print(x,y)

=======
Suggestion 9

def main():
    a,b,d = map(int,input().split())
    print(a,b,d)

=======
Suggestion 10

def main():
    a,b,d = map(int,input().split())
    #print(a,b,d)
    
    import math
    #d = 180 - d
    #print(d)
    #d = math.radians(d)
    #print(d)
    #a = a * math.cos(d) - b * math.sin(d)
    #b = a * math.sin(d) + b * math.cos(d)
    #print(a,b)
    #a = a * math.cos(d) - b * math.sin(d)
    #b = a * math.sin(d) + b * math.cos(d)
    #print(a,b)
    #a = a * math.cos(d) - b * math.sin(d)
    #b = a * math.sin(d) + b * math.cos(d)
    #print(a,b)
    #a = a * math.cos(d) - b * math.sin(d)
    #b = a * math.sin(d) + b * math.cos(d)
    #print(a,b)
    
    #a = a * math.cos(d) - b * math.sin(d)
    #b = a * math.sin(d) + b * math.cos(d)
    #print(a,b)
    
    #a = a * math.cos(d) - b * math.sin(d)
    #b = a * math.sin(d) + b * math.cos(d)
    #print(a,b)
    
    #a = a * math.cos(d) - b * math.sin(d)
    #b = a * math.sin(d) + b * math.cos(d)
    #print(a,b)
    
    #a = a * math.cos(d) - b * math.sin(d)
    #b = a * math.sin(d) + b * math.cos(d)
    #print(a,b)
    
    #a = a * math.cos(d) - b * math.sin(d)
    #b = a * math.sin(d) + b * math.cos(d)
    #print(a,b)
    
    #a = a * math.cos(d) - b * math.sin(d)
    #b = a * math.sin(d) + b * math.cos(d)
    #print(a,b)
    
    #a = a * math.cos(d) - b * math.sin(d)
    #b = a * math.sin(d) + b * math.cos(d)
    #print(a,b)
