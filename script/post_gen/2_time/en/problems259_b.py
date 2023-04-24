Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, d = map(int, input().split())
    print(a * math.cos(math.radians(d)) - b * math.sin(math.radians(d)), a * math.sin(math.radians(d)) + b * math.cos(math.radians(d)))

=======
Suggestion 2

def main():
    from math import sin, cos, radians
    a, b, d = map(int, input().split())
    x = a * cos(radians(d)) - b * sin(radians(d))
    y = a * sin(radians(d)) + b * cos(radians(d))
    print(x, y)

=======
Suggestion 3

def main():
    a, b, d = map(int, input().split())
    d = d / 180 * math.pi
    print(a * math.cos(d) - b * math.sin(d), a * math.sin(d) + b * math.cos(d))

=======
Suggestion 4

def main():
    a, b, d = map(int, input().split())
    rad = math.radians(d)
    a_new = a * math.cos(rad) - b * math.sin(rad)
    b_new = a * math.sin(rad) + b * math.cos(rad)
    print(a_new, b_new)

=======
Suggestion 5

def main():
    a, b, d = map(int, input().split())
    theta = math.radians(d)
    a_prime = a * math.cos(theta) - b * math.sin(theta)
    b_prime = a * math.sin(theta) + b * math.cos(theta)
    print(a_prime, b_prime)

=======
Suggestion 6

def rotate(a, b, d):
    from math import sin, cos, radians
    d = radians(d)
    a, b = a * cos(d) - b * sin(d), a * sin(d) + b * cos(d)
    return a, b

a, b, d = map(int, input().split())
a, b = rotate(a, b, d)
print(a, b)

=======
Suggestion 7

def main():
    import math
    a,b,d=map(int,input().split())
    if d==360:
        print(a,b)
    else:
        d=d*math.pi/180
        a=a*math.cos(d)-b*math.sin(d)
        b=a*math.sin(d)+b*math.cos(d)
        print(a,b)

=======
Suggestion 8

def main():
    # input
    a, b, d = map(int, input().split())
    # compute
    a, b = a * cos(d) - b * sin(d), a * sin(d) + b * cos(d)
    # output
    print(a, b)

=======
Suggestion 9

def main():
    a, b, d = map(int, input().split())
    # a, b, d = map(int, input().split())
    # print(a, b, d)
    d = d * 3.14159265358979323846 / 180
    # print(d)
    # print(a * math.cos(d) - b * math.sin(d), a * math.sin(d) + b * math.cos(d))
    print(a * math.cos(d) - b * math.sin(d), a * math.sin(d) + b * math.cos(d))
