def main():
    X, Y, Z = map(int, input().split())
    if X > Y:
        if Z > 0:
            print(-1)
        else:
            print(X - Y - Z)
    else:
        if Z < 0:
            print(-1)
        else:
            print(Y - X + Z)
