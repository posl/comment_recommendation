def main():
    X,Y,Z = map(int,input().split())
    if X<0 and Y>0:
        if Z<Y:
            print(abs(X)+abs(Z)+abs(Y))
        else:
            print(-1)
    else:
        print(abs(X)-abs(Z))
