def main():
    X, Y, Z = map(int, input().split())
    if X < Y:
        if Z < Y:
            print(abs(X-Z))
        else:
            print(abs(X-Y)+abs(Z-Y))
    else:
        print(-1)

if __name__ == '__main__':
    main()