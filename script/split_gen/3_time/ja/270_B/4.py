def main():
    X, Y, Z = map(int, input().split())
    if X < Y:
        if X < Z:
            print(Z - X)
        else:
            print(-1)
    else:
        print(-1)
