def main():
    X, Y, Z = map(int, input().split())
    if X < Y < Z:
        print(Z - X)
    else:
        print(-1)

if __name__ == '__main__':
    main()