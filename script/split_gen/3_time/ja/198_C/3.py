def main():
    import sys
    input = sys.stdin.readline
    r, x, y = map(int,input().split())
    d = (x**2+y**2)**(1/2)
    if d == r:
        print(1)
    elif d < r:
        print(2)
    else:
        if d % r == 0:
            print(int(d/r))
        else:
            print(int(d/r)+1)
