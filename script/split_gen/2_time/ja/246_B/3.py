def main():
    import sys
    input = sys.stdin.readline
    A, B = map(int, input().split())
    C = (A**2 + B**2)**0.5
    X = A / C
    Y = B / C
    print(X, Y)
