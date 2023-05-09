def main():
    X, Y, Z = map(int, input().split())
    if X > 0 and Y > 0:
        if X < Y:
            print(X - Z)
        else:
            print(X)
    elif X > 0 and Y < 0:
        print(X - Z)
    elif X < 0 and Y > 0:
        print(Y - Z)
    elif X < 0 and Y < 0:
        if X < Y:
            print(X - Z)
        else:
            print(Y - Z)
    else:
        print(-1)
