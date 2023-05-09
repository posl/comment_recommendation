def main():
    X,Y,Z = map(int,input().split())
    if X>0 and Y<0:
        if abs(X)<abs(Y):
            print(abs(X)+abs(Y)-abs(Z))
        else:
            print(abs(X)+abs(Y)+abs(Z))
    elif X<0 and Y>0:
        if abs(X)<abs(Y):
            print(abs(X)+abs(Y)+abs(Z))
        else:
            print(abs(X)+abs(Y)-abs(Z))
    elif X<0 and Y<0:
        if abs(X)<abs(Y):
            print(abs(X)+abs(Y)+abs(Z))
        else:
            print(abs(X)+abs(Y)+abs(Z))
    elif X>0 and Y>0:
        if abs(X)<abs(Y):
            print(abs(X)+abs(Y)-abs(Z))
        else:
            print(abs(X)+abs(Y)-abs(Z))
    else:
        print(-1)
