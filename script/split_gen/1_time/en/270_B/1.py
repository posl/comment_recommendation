def main():
    X, Y, Z = map(int, input().split())
    if X > Y:
        if Z > Y:
            print(X - Y)
        else:
            print(-1)
    else:
        if Z > Y:
            print(-1)
        else:
            print(X - Z)
