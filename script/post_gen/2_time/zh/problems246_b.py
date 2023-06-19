Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    #读取输入
    #A,B = map(int, input().split())
    A,B = 246,402
    #print(A,B)
    #print("A = %d, B = %d" % (A,B))
    #计算
    #h = B / A
    #print("h =

=======
Suggestion 2

def get_distance(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

=======
Suggestion 3

def problems246_b():
    a,b = map(int, input().split())
    print(b/a, 0)

=======
Suggestion 4

def main():
    a,b = map(int,input().split())
    x = a/(a**2+b**2)**0.5
    y = b/(a**2+b**2)**0.5
    print("{:.12f} {:.12f}".format(x,y))

=======
Suggestion 5

def problem246_b():
    A, B = map(int, input().split())
    x = (A**2 + B**2 - 1) / (2*A)
    y = (A**2 + B**2 - 1) / (2*B)
    print(x, y)

=======
Suggestion 6

def get_point(a, b):
    x = 0
    y = 0
    if a == 0:
        x = 0
        y = b
    elif b == 0:
        x = a
        y = 0
    else:
        x = a * b / (a ** 2 + b ** 2) ** 0.5
        y = (a ** 2 - x ** 2) ** 0.5
    return x, y

=======
Suggestion 7

def main():
    A,B = map(int,input().split())
    x = A/((A**2+B**2)**0.5)
    y = B/((A**2+B**2)**0.5)
    print(x,y)

=======
Suggestion 8

def main():
    import sys
    import math

    def solve(A: int, B: int):
        x = B / math.sqrt(A * A + B * B)
        y = A / math.sqrt(A * A + B * B)
        return x, y

    A, B = map(int, input().split())
    ans = solve(A, B)
    print(ans[0], ans[1])

=======
Suggestion 9

def problems246_b():
    A,B = map(int,input().split())
    x = A/(A**2+B**2)**0.5
    y = B/(A**2+B**2)**0.5
    print(x,y)
