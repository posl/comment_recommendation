Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b, d = map(int, input().split())
    d = d * math.pi / 180
    print(a * math.cos(d) - b * math.sin(d), a * math.sin(d) + b * math.cos(d))

=======
Suggestion 2

def main():
    a, b, d = map(int, input().split())
    r = d * math.pi / 180
    print(a * math.cos(r) - b * math.sin(r), a * math.sin(r) + b * math.cos(r))

main()

a, b, d = map(int, input().split())
r = d * math.pi / 180
print(a * math.cos(r) - b * math.sin(r), a * math.sin(r) + b * math.cos(r))

a, b, d = map(int, input().split())
r = d * math.pi / 180
print(a * math.cos(r) - b * math.sin(r), a * math.sin(r) + b * math.cos(r))

a, b, d = map(int, input().split())
r = d * math.pi / 180
print(a * math.cos(r) - b * math.sin(r), a * math.sin(r) + b * math.cos(r))

a, b, d = map(int, input().split())
r = d * math.pi / 180
print(a * math.cos(r) - b * math.sin(r), a * math.sin(r) + b * math.cos(r))

a, b, d = map(int, input().split())
r = d * math.pi / 180
print(a * math.cos(r) - b * math.sin(r), a * math.sin(r) + b * math.cos(r))

a, b, d = map(int, input().split())
r = d * math.pi / 180
print(a * math.cos(r) - b * math.sin(r), a * math.sin(r) + b * math.cos(r))

a, b, d = map(int, input().split())
r = d * math.pi / 180
print(a * math.cos(r) - b * math.sin(r), a * math.sin(r) + b * math.cos(r))

a, b, d = map(int, input().split())
r = d * math.pi / 180
print(a * math.cos(r) - b * math.sin(r), a * math.sin(r) + b * math.cos(r))

a, b, d = map(int, input().split())
r = d * math.pi / 180
print(a * math.cos(r) - b * math.sin(r), a * math.sin(r)

=======
Suggestion 3

def main():
    import math
    a,b,d = map(int,input().split())
    d = math.radians(d)
    x = a * math.cos(d) - b * math.sin(d)
    y = a * math.sin(d) + b * math.cos(d)
    print(x,y)
    return

=======
Suggestion 4

def main():
  a, b, d = map(int, input().split())
  print(a * cos(radians(d)) - b * sin(radians(d)), a * sin(radians(d)) + b * cos(radians(d)))

=======
Suggestion 5

def rotate(x, y, angle):
    import math
    angle = math.radians(angle)
    x1 = x * math.cos(angle) - y * math.sin(angle)
    y1 = x * math.sin(angle) + y * math.cos(angle)
    return x1, y1

a, b, d = map(int, input().split())
x, y = rotate(a, b, d)
print(x, y)

=======
Suggestion 6

def rotate(a,b,d):
    from math import sin,cos,radians
    x=a*cos(radians(d))-b*sin(radians(d))
    y=a*sin(radians(d))+b*cos(radians(d))
    return x,y

a,b,d=map(int,input().split())
print(*rotate(a,b,d))

=======
Suggestion 7

def rotate(x,y,d):
    import math
    d = math.radians(d)
    x = x * math.cos(d) - y * math.sin(d)
    y = x * math.sin(d) + y * math.cos(d)
    return x,y

a,b,d = map(int,input().split())
x,y = rotate(a,b,d)
print(x,y)

=======
Suggestion 8

def main():
    a,b,d = map(int, input().split())
    import math
    d = math.radians(d)
    a,b = a*math.cos(d) - b*math.sin(d), a*math.sin(d) + b*math.cos(d)
    print(a,b)

=======
Suggestion 9

def calc(a, b, d):
    import math
    d = math.radians(d)
    return -1 * (a * math.cos(d) - b * math.sin(d)), a * math.sin(d) + b * math.cos(d)

=======
Suggestion 10

def main():
    a,b,d = map(int, input().split())
    print(a,b)
