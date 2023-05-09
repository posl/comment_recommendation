def main():
    X, Y, Z = map(int, input().split())
    if X > Y:
        print(X - Y)
    else:
        print(-1)
