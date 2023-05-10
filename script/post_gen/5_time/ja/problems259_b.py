Synthesizing 10/10 solutions

=======
Suggestion 1

def input_to_int():
    return [int(i) for i in input().split()]

=======
Suggestion 2

def main():
    a,b,d = input().split()
    a = float(a)
    b = float(b)
    d = float(d)
    import math
    d = math.radians(d)
    x = a*math.cos(d) - b*math.sin(d)
    y = a*math.sin(d) + b*math.cos(d)
    print(x,y)

=======
Suggestion 3

def main():
    import sys
    import math
    a, b, d = map(int, sys.stdin.readline().split())
    rad = math.radians(d)
    x = a * math.cos(rad) - b * math.sin(rad)
    y = a * math.sin(rad) + b * math.cos(rad)
    print(x, y)

main()

=======
Suggestion 4

def main():
    a,b,d = map(int, input().split())
    import math
    rad = d * math.pi / 180.0
    x = a * math.cos(rad) - b * math.sin(rad)
    y = a * math.sin(rad) + b * math.cos(rad)
    print(x,y)

main()

=======
Suggestion 5

def main():
    a,b,d = map(int,input().split())
    rad = d * 3.141592653589793238462643383279502884197169399375105820974944592307816406286 / 180
    print(a * math.cos(rad) - b * math.sin(rad), a * math.sin(rad) + b * math.cos(rad))

=======
Suggestion 6

def rotation(x,y,d):
    import math
    rad = d * math.pi / 180
    return (x*math.cos(rad) - y*math.sin(rad), x*math.sin(rad) + y*math.cos(rad))

a,b,d = map(int,input().split())
x,y = rotation(a,b,d)
print(x,y)

=======
Suggestion 7

def main():
    a,b,d = map(int,input().split())
    import math
    d = math.radians(d)
    x = a*math.cos(d)-b*math.sin(d)
    y = a*math.sin(d)+b*math.cos(d)
    print(x,y)

main()

=======
Suggestion 8

def solve(a,b,d):
    import math
    rad = math.radians(d)
    x = a*math.cos(rad) - b*math.sin(rad)
    y = a*math.sin(rad) + b*math.cos(rad)
    return x,y

=======
Suggestion 9

def main():
    a,b,d = map(int, input().split())
    if d == 0 or d == 360:
        print(a,b)
    elif d == 180:
        print(-a,-b)
    else:
        import math
        x = a*math.cos(math.radians(d)) - b*math.sin(math.radians(d))
        y = a*math.sin(math.radians(d)) + b*math.cos(math.radians(d))
        print(x,y)

=======
Suggestion 10

def main():
    a, b, d = map(int, input().split())
    import math
    d = math.radians(d)
    x = a * math.cos(d) - b * math.sin(d)
    y = a * math.sin(d) + b * math.cos(d)
    print(x, y)
