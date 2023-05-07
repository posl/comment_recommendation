def main():
    X,Y,Z = map(int,input().split())
    if Z < 0:
        print(-1)
    elif abs(X) < abs(Y):
        print(-1)
    else:
        print(abs(X))
