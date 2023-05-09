def main():
    X,Y,Z = map(int,input().split())
    if Z < Y:
        print(-1)
    else:
        print(X/(Z-Y))
