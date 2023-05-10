def main():
    import sys
    import math
    R,X,Y = map(int, sys.stdin.readline().split())
    dist = math.sqrt(X**2 + Y**2)
    if dist < R:
        print(2)
    else:
        print(math.ceil(dist/R))
