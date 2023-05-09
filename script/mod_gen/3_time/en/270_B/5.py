def main():
    X, Y, Z = map(int, input().split())
    if X < Z and Z < Y:
        print(abs(X-Y))
    else:
        print(-1)

if __name__ == '__main__':
    main()