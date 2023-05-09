def main():
    X, Y, Z = map(int, input().split())
    if Z >= X:
        print(-1)
    else:
        print(abs(X-Y))
