def main():
    X,Y,Z = map(int, input().split())
    if Y < Z:
        print(-1)
    else:
        print(int(X/(Y-Z)))

if __name__ == '__main__':
    main()