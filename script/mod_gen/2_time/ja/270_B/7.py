def main():
    X,Y,Z = map(int,input().split())
    if X > 0:
        if Y < 0:
            if Z > 0:
                print(abs(X-Y)+abs(Z-Y))
            else:
                print(abs(X-Y))
        else:
            if Z > 0:
                print(abs(X-Y)+abs(Z-Y))
            else:
                print(-1)
    else:
        if Y < 0:
            if Z > 0:
                print(-1)
            else:
                print(abs(X-Y))
        else:
            if Z > 0:
                print(abs(X-Y)+abs(Z-Y))
            else:
                print(abs(X-Y))

if __name__ == '__main__':
    main()