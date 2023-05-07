def main():
    X,Y,Z = map(int,input().split())
    if X > Y:
        if Z < Y:
            print(-1)
        else:
            print(X-Z)
    else:
        if Z > Y:
            print(-1)
        else:
            print(Z+X)

if __name__ == '__main__':
    main()