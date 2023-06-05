def main():
    #输入
    X,Y,Z = map(int,input().split())
    #判断
    if (X > Y and Y > Z) or (X < Y and Y < Z):
        print(-1)
    else:
        print(abs(X-Z)+abs(Z-Y))
