def main():
    X, Y, Z = map(int, input().split())
    if X < Y:
        X, Y = Y, X
    if X < Z:
        X, Z = Z, X
    if X < Y + Z:
        print(X - Y - Z)
    else:
        print(-1)
