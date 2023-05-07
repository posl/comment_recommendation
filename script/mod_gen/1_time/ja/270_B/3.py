def main():
    X, Y, Z = map(int, input().split())
    if X > Y:
        if Z > Y:
            print(abs(X-Z))
        else:
            print(-1)
    else:
        if Z > X:
            print(abs(Y-Z))
        else:
            print(-1)

if __name__ == '__main__':
    main()