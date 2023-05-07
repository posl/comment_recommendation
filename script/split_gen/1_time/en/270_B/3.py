def main():
    X, Y, Z = [int(x) for x in input().split()]
    if X > 0:
        print(X - Y)
    elif X < 0:
        print(-X + Y)
    else:
        if Z > 0:
            print(Y - Z)
        else:
            print(-Y - Z)
