def main():
    X, Y, Z = map(int, input().split())
    if X > Y:
        if Z > 0:
            print(-1)
        else:
            print(X - Y + abs(Z))
    else:
        print(-1)

if __name__ == '__main__':
    main()