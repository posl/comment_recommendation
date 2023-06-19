def main():
    import sys
    input = sys.stdin.readline
    import math
    R, X, Y = map(int, input().split())
    if X**2 + Y**2 == R**2:
        print(1)
    elif X**2 + Y**2 < R**2:
        print(2)
    else:
        print(math.ceil(math.sqrt(X**2 + Y**2)/R))
main()
