Synthesizing 10/10 solutions (Duplicates hidden)

=======

def main():
    x1, y1, x2, y2 = map(int, input().split())
    x3 = x2 - (y2 - y1)
    y3 = y2 + (x2 - x1)
    x4 = x3 - (x2 - x1)
    y4 = y3 - (y2 - y1)
    print(x3, y3, x4, y4)

=======

def main():
    x1, y1, x2, y2 = map(int, input().split())
    x3 = x2 - (y2 - y1)
    y3 = y2 + (x2 - x1)
    x4 = x1 - (y2 - y1)
    y4 = y1 + (x2 - x1)
    print(x3, y3, x4, y4)

=======

def main():
    x1, y1, x2, y2 = map(int, input().split())
    dx = x2 - x1
    dy = y2 - y1
    x3 = x2 - dy
    y3 = y2 + dx
    x4 = x3 - dx
    y4 = y3 - dy
    print(x3, y3, x4, y4)

main()

=======

def main():
    x1, y1, x2, y2 = map(int, input().split())
    print(x2 - y2 + y1, y2 + x2 - x1, x1 - y2 + y1, y1 + x2 - x1)

=======

def main():
    x1,y1,x2,y2 = map(int,input().split())
    x3 = x2 - y2 + y1
    y3 = y2 + x2 - x1
    x4 = x3 - y3 + y2
    y4 = y3 + x3 - x2
    print(x3,y3,x4,y4)

=======

def solve():
    x1, y1, x2, y2 = map(int, input().split())
    dx = x2 - x1
    dy = y2 - y1
    x3 = x2 - dy
    y3 = y2 + dx
    x4 = x3 - dx
    y4 = y3 - dy
    print(x3, y3, x4, y4)

=======

def main():
    x1,y1,x2,y2 = [int(x) for x in input().split()]
    dx = x2 - x1
    dy = y2 - y1
    x3 = x2 - dy
    y3 = y2 + dx
    x4 = x3 - dx
    y4 = y3 - dy
    print(x3,y3,x4,y4)

=======

def get_input():
    x1, y1, x2, y2 = map(int, input().split())
    return (x1, y1, x2, y2)
