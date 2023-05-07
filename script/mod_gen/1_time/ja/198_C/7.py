def resolve():
    import sys
    import math
    input = sys.stdin.readline
    r,x,y = map(int,input().split())
    if r**2 > x**2 + y**2:
        print(2)
    else:
        print(math.ceil((x**2 + y**2) ** 0.5 / r))

if __name__ == '__main__':
    resolve()